import os

folder_name = "TestFolder"
file_name = "test.txt"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

file_path = os.path.join(folder_name, file_name)
with open(file_path, "w+") as file:
    file.write(f"Hello, it's test file! If you saw this, it means you're interested in my decisions, and I'm glad you're")
    file.seek(0)
    content = file.read()
    print(content)










