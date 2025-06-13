import os
import shutil

def create_backup(source_path, destination_path):
    # Create backup name without extension for make_archive
    backup_name = os.path.join(destination_path, "backup1")
    try:
        shutil.make_archive(backup_name, 'tar', source_path)
        print("Backup created successfully!")
    except Exception as e:
              print(e)
# Correctly formatted paths
source_path = r"C:\Users\suhel\OneDrive\Desktop\Python for Automation\Advance_Topic"
destination_path = r"C:\Users\suhel\OneDrive\Desktop\Python for Automation\backup"

# Call the function
create_backup(source_path, destination_path)
