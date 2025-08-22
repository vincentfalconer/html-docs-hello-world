import os
import shutil

# Define the folders and files to move
folders_to_move = ['css', 'fonts', 'img', 'js']
file_to_move = 'index.html'

# Define the destination folders
static_folder = 'static'
templates_folder = 'templates'

# Create destination folders if they don't exist
os.makedirs(static_folder, exist_ok=True)
os.makedirs(templates_folder, exist_ok=True)

# Move folders into 'static'
for folder in folders_to_move:
    if os.path.exists(folder):
        shutil.move(folder, os.path.join(static_folder, folder))

# Move index.html into 'templates'
if os.path.exists(file_to_move):
    shutil.move(file_to_move, os.path.join(templates_folder, file_to_move))

print("Folders moved to 'static' and index.html moved to 'templates'.")
