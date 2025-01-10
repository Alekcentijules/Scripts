import os

def create_folders_and_files(folder_list: list, file_list: list) -> list:
    try:
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"Folder {folder} created!")
            else:
                print(f"Folder {folder} already exist.")

            for file in file_list:
                file_path = os.path.join(folder, file)
                with open(file_path, "w") as f:
                    f.write(f"It's {file}")

                print(f"Folder '{folder}' and file '{file}' created successfully!")
    except Exception as err:
        print(f"Error creating folder or file: {err}")

def get_user_input():
    user_input_folder = input("Enter folder names separated by a space: ")
    folder_list = user_input_folder.split()
    if not folder_list:
        raise ValueError("No folder names provided!")

    user_input_file = input("Enter file names (without extensions) separated by a space: ")
    file_list = [f"{el}.txt" for el in user_input_file.split()]
    if not file_list:
        raise ValueError("No file names provided!")

    return folder_list, file_list

def main():
    print("Welcome to Folder and File Creator!")
    try:
        folder_list, file_list = get_user_input()
        create_folders_and_files(folder_list, file_list)
        print("All tasks completed successfully!")
    except ValueError as err:
        print(f"Input Error: {err}")
    except Exception as err:
        print(f"Unexpected Error: {err}")

if __name__ == "__main__":
    main()



