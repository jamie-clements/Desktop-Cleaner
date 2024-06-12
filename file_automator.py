from os import scandir, rename  # for directory scanning and renaming
from os.path import splitext, exists, join  # path manipulations
from shutil import move  # to move files
from time import sleep  # for pausing execution

import logging  # for logging events

from watchdog.observers import Observer  # for monitoring file system events
from watchdog.events import FileSystemEventHandler  # for handling file system events

# Source and destination directories
source_dir = "/Users/jamieclements/Downloads"  # Directory to watch for changes
sfx_dir = "/Users/jamieclements/Downloads/sounds"  
music_dir = "/Users/jamieclements/Downloads/music"  
video_dir = "/Users/jamieclements/Downloads/videos"  
image_dir = "/Users/jamieclements/Downloads/images"  
document_dir = "/Users/jamieclements/Downloads/documents"  
code_dir = "/Users/jamieclements/Downloads/code"  

# File extensions
# List of image file extensions
image_exts = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
              ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# List of video file extensions
video_exts = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
              ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# List of audio file extensions
audio_exts = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

# List of document file extensions
document_exts = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# List of code file extensions
code_exts = [".py", ".js", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".php", ".rb", ".go", ".rs", ".ts", ".swift", ".sh", ".bat", ".pl", ".r", ".sql"]

def generate_unique_name(dest, name):
    """
    Generates a unique filename if the file already exists in the destination directory.
    
    Parameters:
    dest (str): Destination directory
    name (str): Original filename
    
    Returns:
    str: Unique filename
    """
    filename, extension = splitext(name)
    counter = 1
    # Loop to find a unique filename by appending a counter
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_to_directory(dest, entry, name):
    """
    Moves a file to the destination directory. If a file with the same name exists,
    it renames the existing file to a unique name.
    
    Parameters:
    dest (str): Destination directory
    entry (DirEntry): Directory entry object
    name (str): Filename
    """
    if exists(f"{dest}/{name}"):
        unique_name = generate_unique_name(dest, name)
        old_path = join(dest, name)
        new_path = join(dest, unique_name)
        rename(old_path, new_path)
    move(entry, dest)

class FileMoverHandler(FileSystemEventHandler):
    """
    Event handler for monitoring and moving files based on their extensions.
    """

    def on_modified(self, event):
        """
        Called when a file or directory is modified. It checks and moves files
        to appropriate directories based on their extensions.
        
        Parameters:
        event (FileSystemEvent): File system event
        """
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.handle_audio_files(entry, name)
                self.handle_video_files(entry, name)
                self.handle_image_files(entry, name)
                self.handle_document_files(entry, name)
                self.handle_code_files(entry, name)

    def handle_audio_files(self, entry, name):
        """
        Checks and moves audio files based on their extensions and size.
        
        Parameters:
        entry (DirEntry): Directory entry object
        name (str): Filename
        """
        for audio_ext in audio_exts:
            if name.endswith(audio_ext) or name.endswith(audio_ext.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # Files less than 10MB or containing 'SFX' are moved to SFX directory
                    dest = sfx_dir
                else:
                    dest = music_dir
                move_to_directory(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def handle_video_files(self, entry, name):
        """
        Checks and moves video files based on their extensions.
        
        Parameters:
        entry (DirEntry): Directory entry object
        name (str): Filename
        """
        for video_ext in video_exts:
            if name.endswith(video_ext) or name.endswith(video_ext.upper()):
                move_to_directory(video_dir, entry, name)
                logging.info(f"Moved video file: {name}")

    def handle_image_files(self, entry, name):
        """
        Checks and moves image files based on their extensions.
        
        Parameters:
        entry (DirEntry): Directory entry object
        name (str): Filename
        """
        for image_ext in image_exts:
            if name.endswith(image_ext) or name.endswith(image_ext.upper()):
                move_to_directory(image_dir, entry, name)
                logging.info(f"Moved image file: {name}")

    def handle_document_files(self, entry, name):
        """
        Checks and moves document files based on their extensions.
        
        Parameters:
        entry (DirEntry): Directory entry object
        name (str): Filename
        """
        for doc_ext in document_exts:
            if name.endswith(doc_ext) or name.endswith(doc_ext.upper()):
                move_to_directory(document_dir, entry, name)
                logging.info(f"Moved document file: {name}")

    def handle_code_files(self, entry, name):
        """
        Checks and moves code files based on their extensions.
        
        Parameters:
        entry (DirEntry): Directory entry object
        name (str): Filename
        """
        for code_ext in code_exts:
            if name.endswith(code_ext) or name.endswith(code_ext.upper()):
                move_to_directory(code_dir, entry, name)
                logging.info(f"Moved code file: {name}")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Path to be monitored
    path = source_dir
    event_handler = FileMoverHandler()  # Initialize event handler
    observer = Observer()  # Initialize observer
    observer.schedule(event_handler, path, recursive=True)  # Schedule observer to monitor the path
    observer.start()  # Start the observer
    try:
        while True:
            sleep(10)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()  # Stop the observer on keyboard interrupt
    observer.join()  # Wait for the observer to finish
