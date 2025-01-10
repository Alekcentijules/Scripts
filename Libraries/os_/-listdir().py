import os

folder_name = "MyLovelyFolder"
file_name = "this_file_in_list.txt"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file_path = os.path.join(folder_name, file_name)
with open(file_path, "w") as file:
    file.write(f"{file_name}")
    print(f"Folder {folder_name} and file {file_name} created!")

files = os.listdir(folder_name)
print(f"Files in '{folder_name}': {files}")







