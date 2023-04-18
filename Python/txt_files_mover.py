import os
import shutil

#! This code reads a text file containing a list of filenames and moves them from a source folder to a destination folder.
#! If the destination folder doesn't exist, it creates it.
#! If a file in the text list is not found in the source folder, it displays an error message.

# TODO Full path to the source folder
source_folder = r"./"
# TODO Full path to the destination folder
destination_folder = r"./Destination Folder"
# TODO Full path to the text file containing the file names
txt_file = r"./filenames_list.txt"

# ? Check if the destination folder exists and create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# ? Move each file from the source folder to the destination folder if its file name is in the text file
with open(txt_file, "r") as f:
    for line in f:
        file_name = line.strip()
        source_file = os.path.join(source_folder, file_name)
        dest_file = os.path.join(destination_folder, file_name)
        if os.path.isfile(source_file):
            # ? Change "move" to "copy2" for copying instead of moving the file
            shutil.move(source_file, dest_file)
            print(f"Moved {file_name} successfully.")
        else:
            print(f"Error: file {file_name} not found in {source_folder}")
