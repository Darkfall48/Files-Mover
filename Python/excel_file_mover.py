import os
import pandas as pd
import shutil

#! This code reads an Excel file containing a list of filenames and moves them from a source folder to a destination folder.
#! If the destination folder doesn't exist, it creates it.
#! If a file in the list is not found in the source folder, it displays an error message.

# TODO Full path to the source folder
source_folder = r"./"
# TODO Full path to the destination folder
destination_folder = r"./Destination Folder"
# TODO Full path to the Excel file
excel_file = r"./picture_list.xlsx"
# TODO Name of the column in the excel file containing the file names
column_name = "Filename"

# ? Check if the destination folder exists and create it if it doesn't
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# ? Move each files from the source folder to the destination folder if its file name is in the Excel file
df = pd.read_excel(excel_file)
for file_name in df[column_name]:
    source_file = os.path.join(source_folder, file_name)
    dest_file = os.path.join(destination_folder, file_name)
    if os.path.isfile(source_file):
        # ? Change "move" to "copyfile" for copying instead of moving the file
        shutil.move(source_file, dest_file)
        print(f"Moved {file_name} successfully.")
    else:
        print(f"Error: file {file_name} not found in {source_folder}")
