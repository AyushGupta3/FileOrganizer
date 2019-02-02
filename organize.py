import os
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm"],
    "DOCUMENTS": [".epub", ".docx", ".doc",".xps", ".dotx", ".docm", ".dox", ".xls", ".xlsx", ".ppt",".pptx"],
    "ARCHIVES": [".iso", ".tar",".7z",".dmg", ".rar", ".zip", ".gz"],
    "AUDIO": [".mp3", ".msv",".raw", ".wav"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "CS": [".py", ".java", ".c"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}
FILE_FORMATS = {file_format: directory for directory, file_formats in DIRECTORIES.items() for file_format in file_formats} 

def organize_files():
    create_directories()
    for file in os.listdir():
        if os.path.isdir(file):
            continue
        filename, fileextension = os.path.splitext(file)
        if fileextension in FILE_FORMATS.keys():
            if not file in os.listdir(FILE_FORMATS[fileextension.lower()]):
                os.rename(file, os.path.join(FILE_FORMATS[fileextension.lower()], file))
    delete_empty_directories()
        
def delete_empty_directories():
    for key in os.listdir():
        if os.path.isdir(key) and not os.listdir(key):
            os.rmdir(key)

def create_directories():
    for key in DIRECTORIES.keys():
        if not os.path.exists(key):
            os.mkdir(key)

if __name__ == "__main__":
    organize_files()