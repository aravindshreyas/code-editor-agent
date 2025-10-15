from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
def main():
    '''working_dir='calculator'
    root_contents=get_files_info(working_dir,".")
    print(root_contents)
    pkg_contents=get_files_info(working_dir,"pkg")
    print(pkg_contents)
    bin_contents=get_files_info(working_dir,"/bin")
    print(bin_contents)
    out_contents=get_files_info(working_dir,"../")
    print(out_contents)'''
    working_dir='calculator'
    print(get_file_content(working_dir,'lorem.txt'))
    print(get_file_content(working_dir,'main.py'))
    print(get_file_content(working_dir,'pkg/calculator.py'))

main()