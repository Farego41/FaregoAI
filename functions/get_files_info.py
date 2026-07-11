import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        #This checks the directory the LLM is asking to access vs the actual directory you want to give it permission to access
        working_directory_abspath = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abspath, directory))
        valid_target_dir = os.path.commonpath([working_directory_abspath, target_dir]) == working_directory_abspath
        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory.'
        if valid_target_dir == False:
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            list_of_strings = []
            for item in os.listdir(target_dir):
               full_path = os.path.join(target_dir,item)
               list_of_strings.append(f'-{item}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}')
            size_and_dir_string = '\n'.join(list_of_strings)
            return size_and_dir_string
    except Exception as e:
       return 'Error: Something went wrong with one of the standard library functions'