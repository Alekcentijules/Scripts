import shutil
import os

folder_list = ["MyOldLovelyFolder", "MyNewLovelyFolder"]
file_name = "source.txt"
copy_file = "source_copy.txt"

for folder in folder_list:
    if not os.path.exists(folder):
        os.makedirs(folder)
file_path = os.path.join(folder_list[0], file_name)
copy_path = os.path.join(folder_list[0], copy_file)
with open(file_path, "w") as file:
    file.write(f"Hello! It's {file_name}")
print(f"Folder {folder_list[0]} and file {file_name} created!")

shutil.copy(file_path, copy_path)
shutil.move("MyOldLovelyFolder/source.txt", "MyNewLovelyFolder/source.txt")