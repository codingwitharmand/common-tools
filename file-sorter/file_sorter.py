import argparse
import os
import shutil
import sys
import logging


def create_sorted_folder(target_directory):
    sorted_folder = os.path.join(target_directory, 'SortedFiles')
    if not os.path.exists(sorted_folder):
        os.makedirs(sorted_folder)


def get_category_for_extension(file_extension, common_extensions):
    for category, extensions in common_extensions.items():
        if file_extension.lower() in extensions:
            return category

    return 'Other'


def sort_files(target_directory, common_extensions):
    files = [file for file in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, file))]

    for file in files:
        file_path = os.path.join(target_directory, file)
        _, file_extension = os.path.splitext(file)

        category = get_category_for_extension(file_extension, common_extensions)
        destination_folder = os.path.join(target_directory, 'SortedFiles', category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, file))
        logging.info(f"Move {file} to {destination_folder}...")


def main():
    parser = argparse.ArgumentParser(description='Sort file in a directory by extension.')
    parser.add_argument('target_directory', help='The directory containing files to be sorted.')
    args = parser.parse_args()

    target_directory = args.target_directory

    if not os.path.exists(target_directory):
        logging.error(f"The specified directory '{target_directory}' does not exist.")
        return

    logging.info(f"Sorting files in {target_directory}...")

    create_sorted_folder(target_directory)

    common_extensions = {
        'Images': ['.png', '.heic', '.jpeg', '.jpg', '.gif', '.bmp', '.webp', '.svg'],
        'Docs': ['.pdf', '.doc', '.docx', '.xlsx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.tar.gz', '.zip'],
        'App': ['.app', '.dmg'],
        'Text': ['.txt', '.json', '.csv', '.yaml', '.html'],
    }

    sort_files(target_directory, common_extensions)

    logging.info("Sorting complete...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
