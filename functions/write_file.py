import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text to a given file and creates the file if needed",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write the content to, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content that is written to the specified file",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file_path = os.path.commonpath([working_directory_abspath, target_file_path]) == working_directory_abspath
        if valid_target_file_path == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path) == True:
            print(f"DEBUG target_file_path: {target_file_path}")
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        #Makes sure all parent directories exist
        os.makedirs(os.path.dirname(target_file_path),exist_ok=True)
        #Writes to the content to the file
        with open(target_file_path, mode='w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return "Error: Something went wrong with the standard library functions"