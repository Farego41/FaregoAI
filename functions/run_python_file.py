import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file_path = os.path.commonpath([working_directory_abspath, target_file_path]) == working_directory_abspath
        if valid_target_file_path == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_file_path) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if target_file_path[-2:] != 'py':
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        if args != None:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output_string_list = []
        if result.returncode != 0:
            output_string_list.append(f'Process exited with code {result.returncode}')
        if result.stdout == None and result.stderr == None:
            output_string_list.append(f'No output produced')
        else:
            output_string_list.append(f'STDOUT: {result.stdout}')
            output_string_list.append(f'STDERR: {result.stderr}')
        return '\n'.join(output_string_list)
    except Exception as e: 
        return "Error: Something went wrong with the standard library functions"