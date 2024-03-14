import os
import shutil

# Define the path to your download folder
download_folder = "/Users/lalithchintakrindi/Downloads"

# Dictionary mapping file extensions to folder names
folder_mapping = {
    "pdf": "PDFs",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "mp3": "Music",
    "wav": "Music",
    "mp4": "Videos",
    "mov": "Videos",
    "zip": "Archives",
    "rar": "Archives",
    "exe": "Executables",
    "dmg": "Disk Images",
    # Add more file extensions and corresponding folder names as needed
}

def organize_files():
    # Iterate over files in the download folder
    for filename in os.listdir(download_folder):
        # Ignore hidden files and folders
        if not filename.startswith('.'):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            # Remove the leading dot from the extension
            extension = extension[1:].lower()
            
            # Check if the file extension is in the folder mapping
            if extension in folder_mapping:
                # Create the destination folder if it doesn't exist
                destination_folder = os.path.join(download_folder, folder_mapping[extension])
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                # Move the file to the destination folder
                source_path = os.path.join(download_folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{folder_mapping[extension]}' folder.")
            else:
                print(f"No folder found for '{filename}', skipping.")

if __name__ == "__main__":
    organize_files()
