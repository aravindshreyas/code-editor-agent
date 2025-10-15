import os

MAX_CHARS=10000
def get_file_content(working_dir,file_path):
    abs_working_dir =  os.path.abspath(working_dir)
    abs_file_path =  os.path.abspath(os.path.join(working_dir,file_path))   
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not present in current directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{abs_file_path} is not a file'
    file_content_string=""
    try:
        with open(abs_file_path,"r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string)>=MAX_CHARS:
                file_content_string+= f'file {file_path} cut at {MAX_CHARS} characters'
    except Exception as e:
        print(f'Exception {e} raised')

    return file_content_string