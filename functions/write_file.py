import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file_path = os.path.commonpath([working_directory_abspath, target_file_path]) == working_directory_abspath
        if valid_target_file_path == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        #Makes sure all parent directories exist
        os.makedirs(file_path,exist_ok=True)
        #Writes to the content to the file
        with open(target_file_path, mode='w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return "Error: Something went wrong with the standard library functions"