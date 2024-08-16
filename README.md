# Desktop Cleaner

Download AutoSorter is a Python-based automation tool designed to help you keep your Downloads folder organised. By monitoring the Downloads directory, this script automatically moves files into appropriate subdirectories based on their file extensions. This ensures that your files are neatly categorized without manual intervention.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Stopping the Script](#stopping-the-script)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated File Organization:** Moves audio, video, image, document, and code files to their respective directories.
- **Unique Filename Handling:** Ensures files with duplicate names are renamed to avoid overwriting.
- **Background Operation:** Runs as a background process to continuously monitor and organize your Downloads folder.
- **Customizable Directories:** Easily configure source and destination directories to suit your needs.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/file-automator.git
   cd file-automator
   ```

2. **Install Required Packages:**

   The script requires the `watchdog` package for monitoring file system events. You can install it using pip:

   ```sh
   pip install watchdog
   ```

## Usage

1. **Edit the Script:**

   Open `file_automator.py` in a text editor and ensure the source and destination directories are set to your desired paths:

   ```python
   source_dir = "/Users/jamieclements/Downloads"  # Directory to watch for changes
   sfx_dir = "/Users/jamieclements/Downloads/sounds"
   music_dir = "/Users/jamieclements/Downloads/music"
   video_dir = "/Users/jamieclements/Downloads/videos"
   image_dir = "/Users/jamieclements/Downloads/images"
   document_dir = "/Users/jamieclements/Downloads/documents"
   code_dir = "/Users/jamieclements/Downloads/code"
   ```

2. **Run the Script in the Background:**

   Use `nohup` to run the script in the background:

   ```sh
   nohup python file_automator.py &
   ```

   This command will start the script and keep it running in the background, even if you close the terminal.

3. **Check Logs:**

   The `nohup` command will create a file named `nohup.out` in the current directory. You can check the logs with:

   ```sh
   cat nohup.out
   ```

## Stopping the Script

To stop the script when you no longer want it running:

1. **Find the Process ID (PID):**

   ```sh
   ps aux | grep file_automator.py
   ```

   Example output:

   ```
   yourusername 12345  0.0  0.1  2432768  12344   ?  S    12:34   0:00 python file_automator.py
   yourusername 12346  0.0  0.0  2432768   1234   ?  S    12:34   0:00 grep file_automator.py
   ```

2. **Kill the Process:**

   ```sh
   kill 12345
   ```

   Replace `12345` with the actual PID from the previous step.

3. **Verify the Process is Stopped:**

   ```sh
   ps aux | grep file_automator.py
   ```

   Ensure there is no output related to `file_automator.py`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
