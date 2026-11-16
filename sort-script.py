#file sorting project

import os
import shutil
import sys
import time
from pathlib import Path

files_to_move = 0
files_moved = 0

home_dir = Path.home()
downloads_dir = home_dir / "Downloads"

if not os.path.exists(downloads_dir):
    print("Error: Cannot find downloads directory. Exiting program in 3 seconds")
    time.sleep(3)
    sys.exit()
else:
    print(downloads_dir)
    print("Downloads directory found. Beginning program.")

file_extensions_map ={
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".png",".jpg", ".jpeg", ".webp", ".gif", ".avif", ".jpe"],
    "Installers-Compressed files": [".exe",".msi", ".zip"],
    "Audio Files": [".mp3",".wav",".aif",".aiff",".flac",".m4a",".mid",".ogg"],
    "Videos": [".mp4",".mov",".avi",".webm",".mkv",".wmv"],
    "Mod Files": [".jar", ".mrpack",".litematic",".schem"]

}


exemptions_list = []

#dry run

for filename in os.listdir(downloads_dir):
    full_path = os.path.join(downloads_dir, filename)
    if os.path.isfile(full_path):
        name, extension = os.path.splitext(filename)
        print("Found file of name",name,"and extension",extension)
        if filename.lower() in exemptions_list:
                continue
        supported = False

        for folder_name, extensions_list in file_extensions_map.items():
            if extension.lower() in extensions_list:
                supported = True
                target_folder_path = os.path.join(downloads_dir, folder_name)
                destination_path = os.path.join(target_folder_path, filename)
                print("File",filename,"will be moved to",target_folder_path)
                files_to_move += 1
        if not supported:
            print(f"'{name}' has an unsupported extension '{extension}' so will be skipped")

#user confirmation

print("If you continue,",files_to_move,"file(s) will be moved.")
runCheck = input("Are you happy with these changes? (y/n) ")
if not runCheck.lower() == "y":
    sys.exit()

#execution

for filename in os.listdir(downloads_dir):
    full_path = os.path.join(downloads_dir, filename)
    if os.path.isfile(full_path):
        name, extension = os.path.splitext(filename)
        if filename.lower() in exemptions_list:
                continue
        for folder_name, extensions_list in file_extensions_map.items():
            if extension.lower() in extensions_list:
                target_folder_path = os.path.join(downloads_dir, folder_name)

                if not os.path.exists(target_folder_path):
                    print("Creating folder path",target_folder_path)
                    os.makedirs(target_folder_path)
                
                destination_path = os.path.join(target_folder_path, filename)
                counter = 1

                while os.path.exists(destination_path):
                   name, extension = os.path.splitext(filename)
                   new_filename = f"{name} ({counter}){extension}"
                   destination_path = os.path.join(target_folder_path, new_filename)
                   counter += 1
                shutil.move(full_path, destination_path)
                print("Moved",filename,"to",target_folder_path)
                files_moved += 1

#confirmation

if not files_moved == 0:
    print(files_moved,"file(s) succesfully moved")
else:
    print("No files modified.")

print("Exiting automatically in: ", end="", flush=True)
for i in range(3, 0, -1):
    print(f"{i}... ", end="", flush=True)
    time.sleep(1)
print("Goodbye!")
sys.exit()
