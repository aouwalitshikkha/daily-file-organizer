import os
import shutil
from datetime import datetime

current_path = os.getcwd()

today_folder_name = datetime.now().strftime("%Y-%m-%d")
today_folder_path = os.path.join(current_path, today_folder_name)

os.makedirs(today_folder_path, exist_ok=True)

today_date = datetime.now().date()

# Get this script filename
script_name = os.path.basename(__file__)

def created_today(path):
    created_time = os.path.getctime(path)
    created_date = datetime.fromtimestamp(created_time).date()
    return created_date == today_date

for item in os.listdir(current_path):
    item_path = os.path.join(current_path, item)

    # Skip today's folder
    if item == today_folder_name:
        continue

    # Skip the script itself
    if item == script_name:
        continue

    if created_today(item_path):
        shutil.move(item_path, today_folder_path)

print(f"✅ Done! Moved today's files/folders into: {today_folder_path}")
