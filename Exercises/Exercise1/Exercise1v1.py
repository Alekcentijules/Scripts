import os

user_input_folder = input("Enter the name for each folder separated by a space: ")
user_input_file = input("Enter the name for each file separated by a space: ")
folder_list = user_input_folder.split()
file_list = [el + ".txt" for el in user_input_file.split()]

for folder in folder_list:
    if not os.path.exists(folder):
        os.makedirs(folder)
    for file in file_list:
        file_path = os.path.join(folder, file)
        with open(file_path, "w") as f:
            f.write("It's {}".format(file))
        print(f"Folder '{folder}' and file '{file}' created!")

