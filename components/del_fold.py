from tkinter import *
from customtkinter import *
from transfer import delete_empty_folders

class Del_fold(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, corner_radius=0)

        self.label_path = CTkLabel(self,
                                          text="The path")
        self.label_path.pack(anchor=W, padx=50, pady=(15,0))

        self.entry_path = CTkEntry(self,
                                          placeholder_text="Enter the path for the folder using \\\\", 
                                          width=500)
        self.entry_path.pack(anchor=W, padx=50, pady=(0,5))

        self.button_fold_sel = CTkButton(self,
                           text="Path Selection",
                           command=lambda : self.open_folder_selection(self.entry_path))
        self.button_fold_sel.pack(anchor=E, padx=50)

        self.button_start = CTkButton(self,
                           text="Delete Folders",
                           command=self.del_empty_fol)
        self.button_start.pack(anchor=N, padx=50, pady=10)

        self.pack(expand=True, fill=BOTH)

    def del_empty_fol(self):
        folder_path = self.entry_path.get()
        delete_empty_folders(folder_path)

    def open_folder_selection(self, entry_id):
        folder_path = filedialog.askdirectory()
        entry_id.delete(0, "end")
        entry_id.insert(0, folder_path)