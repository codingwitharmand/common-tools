import unittest
import os
import shutil
from file_sorter import create_sorted_folder, get_category_for_extension, sort_files


class TestFileSorter(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir)

        test_files = [
            'file1.txt',
            'image1.jpg',
            'document1.pdf',
            'video1.mp4',
            'music1.mp3',
            'unknown_file.xyz'
        ]

        for file_name in test_files:
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write("This is a test file.")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_create_sorted_folder(self):
        create_sorted_folder(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'SortedFiles')))

    def test_get_category_for_extension(self):
        common_extensions = {
            'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
            'Documents': ['.doc', '.docx', '.pdf', '.txt'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Music': ['.mp3', '.wav', '.flac'],
        }

        self.assertEqual(get_category_for_extension('.jpg', common_extensions), 'Images')
        self.assertEqual(get_category_for_extension('.pdf', common_extensions), 'Documents')
        self.assertEqual(get_category_for_extension('.mp4', common_extensions), 'Videos')
        self.assertEqual(get_category_for_extension('.mp3', common_extensions), 'Music')

        self.assertEqual(get_category_for_extension('.xyz', common_extensions), 'Other')

    def test_sort_files(self):
        common_extensions = {
            'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
            'Documents': ['.doc', '.docx', '.pdf', '.txt'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Music': ['.mp3', '.wav', '.flac'],
        }

        create_sorted_folder(self.test_dir)
        sort_files(self.test_dir, common_extensions)

        sorted_files_dir = os.path.join(self.test_dir, 'SortedFiles')
        for category in common_extensions.keys():
            category_dir = os.path.join(sorted_files_dir, category)
            self.assertTrue(os.path.exists(category_dir))
            files_in_category = os.listdir(category_dir)
            self.assertGreater(len(files_in_category), 0)


if __name__ == '__main__':
    unittest.main()
