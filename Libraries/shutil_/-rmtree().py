import os
import shutil

folder_name = "ThisFolderCannotExist"
file_name = "this_file_cannot_exist.txt"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file_path = os.path.join(folder_name, file_name)
with open(file_path, "w") as file:
    file.write(f"{file_name}")
    print(f"Folder {folder_name} and file {file_name} created and removed!")

del_folder_with_files = shutil.rmtree(folder_name)














