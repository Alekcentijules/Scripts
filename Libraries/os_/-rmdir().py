import os

my_folder = "ThisFolderCannotExist"

if not os.path.exists(my_folder):
    os.makedirs(my_folder)

del_folder = os.rmdir("ThisFolderCannotExist")










