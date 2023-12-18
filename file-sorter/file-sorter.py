import os
import shutil
import sys

def sort_files_by_extension(target_directory):
    sorted_folder = os.path.join(target_directory, 'SortedFiles')
    if not os.path.exists(sorted_folder):
        os.makedirs(sorted_folder)

    files = [file for file in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, file))]

    common_extensions = {
        'Images': ['.png', '.heic', '.jpeg', '.jpg', '.gif', '.bmp', '.webp', '.svg'],
        'Docs': ['.pdf', '.doc', '.docx', '.xlsx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.tar.gz', '.zip'],
        'App': ['.app', '.dmg'],
        'Text': ['.txt', '.json', '.csv', '.yaml', '.html'],
    }

    for file in files:
        file_path = os.path.join(target_directory, file)

        _, file_extension = os.path.splitext(file)

        found = False
        for category, extensions in common_extensions.items():
            if file_extension.lower() in extensions:
                destination_folder = os.path.join(sorted_folder, category)
                found = True
                break

        if not found:
            destination_folder = os.path.join(sorted_folder, 'Other')

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, file))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file-sorter.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]

    if not os.path.exists(target_directory):
        print(f"Error: The specified directory '{target_directory}' doesn't exist.")
        sys.exit(1)

    sort_files_by_extension(target_directory)
