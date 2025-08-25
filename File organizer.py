import os
import shutil

# Replace this with the path to the folder you want to organize
directory : str = r""  # Use raw string (r"") for Windows paths

# Define file type categories
file_types : dict = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Others": [], # Create a folder for uncategorized files
}

# Organizes all files in the given directory. When there is a folder in the firectory it goes through that as well (recursive)
def organize_all_files_in_directory(directory_path: str) -> None:
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isdir(file_path):
                organize_all_files_in_directory(file_path)
                continue
            
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                moved = False

                for folder, extensions in file_types.items():
                    if file_ext in extensions:
                        target_folder = os.path.join(directory, folder)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_folder, filename))
                        print(f"Moved: {filename} → {folder}")
                        moved = True
                        break

                if not moved:
                    other_folder = os.path.join(directory, "Others")
                    os.makedirs(other_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(other_folder, filename))
                    print(f"Moved: {filename} → Others")
    except Exception as e:
        print(f"❌ Error: {e}")



input_directory_path : str = input("Please enter path to the directory to sort: \n")


if os.path.isdir(input_directory_path):
    directory = input_directory_path
else:
    print("Please enter valid path")
    exit()


organize_all_files_in_directory(directory)



print("✅ Files organized successfully!")