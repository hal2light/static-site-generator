import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"

def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    if os.path.exists(dir_path_docs):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_docs)
    
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursive("./content", "./template.html",dir_path_docs, basepath)


main()
