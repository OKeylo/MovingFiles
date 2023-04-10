from pathlib import *
import shutil

def move_files(folder_path:str, folder_name:str, files_path:str, files_extension:str):
    fol_path = Path(folder_path, folder_name)
    f_path = Path(files_path)

    if not fol_path.is_dir():
        fol_path.mkdir()

    for file in f_path.glob(f"*.{files_extension}"):
        print(file)
        shutil.move(Path(f_path, file), fol_path)

def delete_empty_folders(folder_path:str, folder_name:str):
    fol_path = Path(folder_path, folder_name)
    for item in fol_path.iterdir():
        try:
            if (item.is_dir()):
                item.rmdir()
        except OSError:
            continue