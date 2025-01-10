import os
import shutil

source_folder = "SortingFolder"
folders = {
    "Image": [".jpg", ".png", ".gif"],
    "Documents": [".txt", ".docx", ".pdf"],
    "Music": [".mp3", ".wav"]
}

os.makedirs(source_folder, exist_ok=True)
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder_name, extensions in folders.items():
            if file.endswith(tuple(extensions)):
                target_folder = os.path.join(source_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)
                print(f"Moved {file} to {target_folder}")
                break









