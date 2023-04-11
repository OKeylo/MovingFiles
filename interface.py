from tkinter import *
from customtkinter import *
from transfer import move_files_same_extension, delete_empty_folders
from components.del_fold import Del_fold

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("MovingFiles")
        self.iconbitmap('document.ico')

        #selection menu
        self.selection = CTkFrame(self, corner_radius=0)

        segment_button_var = StringVar(value="Move_files")
        self.segment_button = CTkSegmentedButton(self.selection,
                                                 values=["Move_files", "Delete_folders", "Help"],
                                                 variable=segment_button_var)
        self.segment_button.pack(pady=(20,0))

        self.selection.pack(fill=BOTH)

        #main program
        self.frame = CTkFrame(self, corner_radius=0)

        self.label_folder_path = CTkLabel(self.frame,
                                          text="The path for the folder")
        self.label_folder_path.pack(anchor=W, padx=50, pady=(15,0))

        self.entry_folder_path = CTkEntry(self.frame,
                                          placeholder_text="Enter the path for the folder using \\\\", 
                                          width=500)
        self.entry_folder_path.pack(anchor=W, padx=50, pady=(0,5))

        self.label_folder_name = CTkLabel(self.frame,
                                          text="Folder name")
        self.label_folder_name.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_folder_name = CTkEntry(self.frame, 
                                          placeholder_text="Enter a folder name", 
                                          width=500)
        self.entry_folder_name.pack(anchor=W, padx=50, pady=(0,5))

        self.label_files_path = CTkLabel(self.frame,
                                         text="The path from where the files will be moved")
        self.label_files_path.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_files_path = CTkEntry(self.frame, 
                                          placeholder_text="Enter the path from where the files will be moved using \\\\", 
                                          width=500)
        self.entry_files_path.pack(anchor=W, padx=50, pady=(0,5))

        self.label_files_extension = CTkLabel(self.frame,
                                              text="Files extension")
        self.label_files_extension.pack(anchor=W, padx=50, pady=(0,0))

        self.entry_files_extension = CTkEntry(self.frame, 
                                          placeholder_text="Enter the files extension", 
                                          width=500)
        self.entry_files_extension.pack(anchor=W, padx=50, pady=(0,10))

        self.button_start = CTkButton(self.frame,
                           text="Start",
                           command=self.move_files_same_ext)
        self.button_start.pack(anchor=SE, padx=50)

        self.button_start = CTkButton(self.frame,
                           text="Delete Folders",
                           command=self.del_empty_fol)
        self.button_start.pack(anchor=SE, padx=50, pady=10)

        self.label_appearance = CTkLabel(self.frame,
                          text="Appearance Mode")
        self.label_appearance.pack(anchor=SW, padx=25)

        self.combobox_var = StringVar(value="system")
        self.combobox = CTkComboBox(self.frame,
                              values=["system", "light", "dark"],
                              command=self.set_appearance,
                              variable=self.combobox_var)
        self.combobox.pack(anchor=SW, padx=10)

        #self.test = Del_fold(self.frame)

        self.frame.pack(expand=True, fill=BOTH)


        #starting our application
        self.start_app()

    def set_appearance(self, choice):
        set_appearance_mode(choice)

    def move_files_same_ext(self):
        folder_path = self.entry_folder_path.get()
        folder_name = self.entry_folder_name.get()
        files_path = self.entry_files_path.get()
        files_extension = self.entry_files_extension.get()
        move_files_same_extension(folder_path, folder_name, files_path, files_extension)
    
    def del_empty_fol(self):
        folder_path = self.entry_folder_path.get()
        folder_name = self.entry_folder_name.get()
        delete_empty_folders(folder_path, folder_name)
    
    def start_app(self):
        self.mainloop()

