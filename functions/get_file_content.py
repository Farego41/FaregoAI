import os
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Writes the content of a file to a string, up to MAX_CHARS (currently 10000)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get content from",
                },
            },
        },
        "required": ["file_path"]
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file_path = os.path.commonpath([working_directory_abspath, target_file_path]) == working_directory_abspath
        if valid_target_file_path == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        #Opens the file, reads its contents into a string, closes the file (due to the with statement).
        with open(target_file_path, mode='r') as f:
            file_content_string = f.read(MAX_CHARS)
            #Determines if the file was truncated
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e: 
        return "Error: Something went wrong with the standard library functions"