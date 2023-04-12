from tkinter import *
from customtkinter import *
from transfer import move_files_same_extension

class Move_fls(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        
        self.label_folder_path = CTkLabel(self,
                                          text="The path for the folder")
        self.label_folder_path.pack(anchor=W, padx=50, pady=(15,0))

        self.entry_folder_path = CTkEntry(self,
                                          placeholder_text="Enter the path for the folder using \\\\", 
                                          width=500)
        self.entry_folder_path.pack(anchor=W, padx=50, pady=(0,5))

        self.label_folder_name = CTkLabel(self,
                                          text="Folder name")
        self.label_folder_name.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_folder_name = CTkEntry(self, 
                                          placeholder_text="Enter a folder name", 
                                          width=500)
        self.entry_folder_name.pack(anchor=W, padx=50, pady=(0,5))

        self.label_files_path = CTkLabel(self,
                                         text="The path from where the files will be moved")
        self.label_files_path.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_files_path = CTkEntry(self, 
                                          placeholder_text="Enter the path from where the files will be moved using \\\\", 
                                          width=500)
        self.entry_files_path.pack(anchor=W, padx=50, pady=(0,5))

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
        self.button_start.pack(anchor=SE, padx=50)

        self.label_appearance = CTkLabel(self,
                          text="Appearance Mode")
        self.label_appearance.pack(anchor=SW, padx=25)

        self.combobox_var = StringVar(value="system")
        self.combobox = CTkComboBox(self,
                              values=["system", "light", "dark"],
                              command=self.set_appearance,
                              variable=self.combobox_var)
        self.combobox.pack(anchor=SW, padx=10)

        self.pack(expand=True, fill=BOTH)

    def set_appearance(self, choice):
        set_appearance_mode(choice)

    def move_files_same_ext(self):
        folder_path = self.entry_folder_path.get()
        folder_name = self.entry_folder_name.get()
        files_path = self.entry_files_path.get()
        files_extension = self.entry_files_extension.get()
        move_files_same_extension(folder_path, folder_name, files_path, files_extension)