import os
import shutil

# Replace this with the path to the folder you want to organize
directory = r"C:\Users\shuda\Downloads"  # Use raw string (r"") for Windows paths

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

# Create a folder for uncategorized files
file_types["Others"] = []

try:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

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

    print("✅ Files organized successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
