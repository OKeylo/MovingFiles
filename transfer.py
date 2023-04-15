from pathlib import *
import shutil

def move_files_same_extension(folder_path:str, files_path:str, files_extension:str):
    fol_path = Path(folder_path)
    f_path = Path(files_path)

    if not fol_path.is_dir():
        fol_path.mkdir()

    for file in f_path.glob(f"*.{files_extension}"):
        print(file)
        shutil.move(Path(f_path, file), fol_path)

def delete_empty_folders(folder_path:str):
    fol_path = Path(folder_path)
    
    for item in fol_path.rglob("*"):
        try:
            if (item.is_dir()):
                item.rmdir()
        except OSError:
            continue