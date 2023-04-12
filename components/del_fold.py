from tkinter import *
from customtkinter import *
from transfer import delete_empty_folders

class Del_fold(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)

        self.label_folder_path = CTkLabel(self,
                                          text="The path for the folder")
        self.label_folder_path.pack(anchor=W, padx=50, pady=(15,0))

        self.entry_folder_path = CTkEntry(self,
                                          placeholder_text="Enter the path for the folder using \\\\", 
                                          width=500)
        self.entry_folder_path.pack(anchor=W, padx=50, pady=(0,5))

        self.button_start = CTkButton(self,
                           text="Delete Folders",
                           command=self.del_empty_fol)
        self.button_start.pack(anchor=SE, padx=50, pady=10)

        self.pack(expand=True, fill=BOTH)

    def del_empty_fol(self):
        folder_path = self.entry_folder_path.get()
        delete_empty_folders(folder_path)