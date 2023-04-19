# Files Mover

- This code allows you to move or copy a list of files from a source folder to a destination folder using an Excel, CSV, or TXT file as the list of file names.
- It creates the destination folder if it doesn't exist and displays an error message for any file in the list that is not found in the source folder.
- It can handle any type of file.

# Instructions

_You can also modify the code to copy files instead of moving them by changing the `shutil.move()` function to `shutil.copyfile()`._

1. Install Python (https://www.python.org/downloads/)

### TXT File

_The TXT file should contain only the file names, with one file name per line._

2. Modify the `source_folder`, `destination_folder`, and `txt_file` variables in the code to your desired file paths.
3. To execute the script, run the command:

```
python txt_file_mover.py
```

### CSV File

_The CSV file should contain only the file names in the first column, without a header._

2. Modify the `source_folder`, `destination_folder`, and `csv_file` variables in the code to your desired file paths.
3. To execute the script, run the command:

```
python csv_file_mover.py
```

### Excel File

_The Excel file should contain only the file names in a single column, with a header that matches the `column_name` variable in the code._

2. Modify the `source_folder`, `destination_folder`, `excel_file`, and `column_name` variables in the code to your desired file paths and column name.
3. Install the `pandas` and `openpyxl` libraries if it's not already installed by running:

```
pip install pandas openpyxl
```

4. To execute the script, run the command:

```
python excel_file_mover.py
```
