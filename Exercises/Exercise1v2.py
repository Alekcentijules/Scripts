import os

def create_folders_and_files(folder_list: list, file_list: list) -> list:
    for folder in folder_list:
        if not os.path.exists(folder):
            os.makedirs(folder)

        for file in file_list:
            file_path = os.path.join(folder, file)
            with open(file_path, "w") as f:
                f.write(f"It's {file}")

            print(f"Folder '{folder}' and file '{file}' created successfully!")


def main():
    user_input_folder = input("Enter folder names separated by a space: ")
    folder_list = user_input_folder.split()
    if not folder_list:
        print("Error: No folder names provided!")
        return

    user_input_file = input("Enter file names (without extensions) separated by a space: ")
    file_list = [f"{el}.txt" for el in user_input_file.split()]
    if not file_list:
        print("Error: No file names provided!")
        return

    create_folders_and_files(folder_list, file_list)

if __name__ == "__main__":
    main()















