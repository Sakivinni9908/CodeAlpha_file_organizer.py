import os
import shutil

# Source folder containing JPG files
source_folder = "source_images"

# Destination folder
destination_folder = "jpg_images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get all files from the source folder
files = os.listdir(source_folder)

# Move JPG files
for file in files:

    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("\nAll JPG files have been moved successfully!")