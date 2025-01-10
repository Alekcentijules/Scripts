import os
import shutil

source_folder = "SortingFolder"
folders = {
    "Image": [".jpg", ".png", ".gif"],
    "Documents": [".txt", ".docx", ".pdf"],
    "Music": [".mp3", ".wav"]
}

# print(os.listdir(source_folder))
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    print(file)