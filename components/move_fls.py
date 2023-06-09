from tkinter import *
from customtkinter import *
from transfer import move_files_same_extension

class Move_fls(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, corner_radius=0)
        
        self.label_origin_path = CTkLabel(self,
                                         text="Origin path")
        self.label_origin_path.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_origin_path = CTkEntry(self, 
                                          placeholder_text="Enter the path from where the files will be moved using \\\\", 
                                          width=500)
        self.entry_origin_path.pack(anchor=W, padx=50, pady=(0,5))

        self.button_path_sel = CTkButton(self,
                           text="Path Selection",
                           command=lambda: self.open_folder_selection(self.entry_origin_path))
        self.button_path_sel.pack(anchor=E, padx=50)

        self.label_destination_path = CTkLabel(self,
                                          text="Destination path")
        self.label_destination_path.pack(anchor=W, padx=50, pady=(15,0))

        self.entry_destination_path = CTkEntry(self,
                                          placeholder_text="Enter the path where the files will be moved to using \\\\", 
                                          width=500)
        self.entry_destination_path.pack(anchor=W, padx=50, pady=(0,5))

        self.button_fold_sel = CTkButton(self,
                           text="Path Selection",
                           command=lambda : self.open_folder_selection(self.entry_destination_path))
        self.button_fold_sel.pack(anchor=E, padx=50)

        self.label_files_extension = CTkLabel(self,
                                              text="Files extension")
        self.label_files_extension.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_files_extension = CTkEntry(self, 
                                          placeholder_text="Enter the files extension", 
                                          width=500)
        self.entry_files_extension.pack(anchor=W, padx=50, pady=(0,10))

        self.button_start = CTkButton(self,
                           text="Start",
                           command=self.move_files_same_ext)
        self.button_start.pack(anchor=N, padx=50)

        self.pack(expand=True, fill=BOTH)

    def move_files_same_ext(self):
        origin_path = self.entry_origin_path.get()
        destination_path = self.entry_destination_path.get()
        files_extension = self.entry_files_extension.get()
        move_files_same_extension(destination_path, origin_path, files_extension)

    def open_folder_selection(self, entry_id):
        folder_path = filedialog.askdirectory()
        entry_id.delete(0, "end")
        entry_id.insert(0, folder_path)
