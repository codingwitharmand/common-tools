# File Sorter

The File Sorter is a Python script that organizes files in a specified directory based on their extensions. It categorizes files into folders such as Images, Documents, Videos, Music, App, Archive and Other.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/codingwitharmand/common-tools.git
   cd file-sorter
   ```

2. **Run the Script:**

   ```bash
   python sorter.py /path/to/target_directory
   ```

   Replace `/path/to/target_directory` with the path to the directory you want to sort.

3. **Check the Results:**

   The script will create a new folder named `SortedFiles` within the target directory and organize files based on their extensions. The log statements will provide information about the sorting process.

## Configuration

You can customize the file extensions and categories by modifying the `common_extensions` dictionary in the `sorter.py` script.

```python
common_extensions = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.flac'],
}
```

## Requirements

- Python 3.x

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.html) file for details.