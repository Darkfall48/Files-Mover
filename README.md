# Files Mover

- This code allows you to move or copy a list of files from a source folder to a destination folder using an Excel, CSV, or TXT file as the list of file names.
- It creates the destination folder if it doesn't exist and displays an error message for any file in the list that is not found in the source folder.
- It can handle any type of file.

# Instructions

## CSV File

1. Modify the `source_folder`, `destination_folder`, and `csv_file` variables in the code to your desired file paths.
2. To execute the script, run the command:
```
python csv_file_mover.py
```

## Excel File

1. Modify the `source_folder`, `destination_folder`, `excel_file`, and `column_name` variables in the code to your desired file paths and column name.
2. Install the `pandas` and `openpyxl` libraries if it's not already installed by running:
```
pip install pandas openpyxl
```
2. To execute the script, run the command:
```
python excel_file_mover.py
```




