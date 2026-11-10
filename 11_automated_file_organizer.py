
# Project: Automated File Organizer

import os
import shutil

# Define source directory
SOURCE_FOLDER = "downloads"

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Python": [".py"],
    "Archives": [".zip", ".rar"]
}


# Function to identify file category
def get_file_category(filename):

    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"


# Function to create folders
def create_folder(folder_path):

    os.makedirs(folder_path, exist_ok=True)


# Function to organize files
def organize_files():

    if not os.path.isdir(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    total_files = 0
    organized_files = 0

    print("===== FILE ORGANIZATION STARTED =====")

    for filename in os.listdir(SOURCE_FOLDER):

        source_path = os.path.join(SOURCE_FOLDER, filename)

        # Skip directories
        if not os.path.isfile(source_path):
            continue

        total_files += 1

        category = get_file_category(filename)

        destination_folder = os.path.join(
            SOURCE_FOLDER, category
        )

        create_folder(destination_folder)

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Handle duplicate filenames
        if os.path.exists(destination_path):
            print("Skipped duplicate:", filename)
            continue

        try:

            shutil.move(source_path, destination_path)

            organized_files += 1

            print(filename, "->", category)

        except OSError as error:

            print("Error moving file:", filename, error)

    # Display summary
    print("\n===== ORGANIZATION SUMMARY =====")

    print("Total Files Found:", total_files)
    print("Successfully Organized:", organized_files)
    print("Skipped Files:", total_files - organized_files)

    print("\nFile organization completed.")


# Main execution
if __name__ == "__main__":
    organize_files()
