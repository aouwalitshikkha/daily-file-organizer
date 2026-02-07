# Move Today’s Files into a Date Folder

This script is a simple daily cleanup tool.

When you run it inside any folder, it will scan that folder and find all files and folders that were created today. Then it creates a new folder named with today’s date (format: YYYY-MM-DD) and moves everything created today into it.

Example folder name:
2026-02-07

## What it does

If your folder looks like this:

Work/
report.docx
new_project/
old_notes.txt
organize.py

And report.docx + new_project/ were created today, after running the script it becomes:
```text
Work/
2026-02-07/
report.docx
new_project/
old_notes.txt
organize.py
```

Folders are moved as folders, so the structure inside them is not changed.

## How to run

Run the script inside the folder you want to organize.

Windows:
```
python organize.py
```
Mac/Linux:
```
python3 organize.py
```

## Important Notes

* The script does not move the folder it creates (YYYY-MM-DD).
* The script does not move itself.
* Everything else created today will be moved.

## OS Warning

This script uses os.path.getctime() to detect creation date.

On Windows:

* getctime() returns the real creation time, so it works correctly.

On macOS / Linux:

* getctime() may return metadata change time instead of true creation time.
* If you want reliable behavior on macOS/Linux, using modified time may be a better option.

## Why this script exists

To avoid manually creating a “today” folder and dragging files into it every day. Running the script does the same thing automatically.
