from tkinter import *
from customtkinter import *
from components.del_fold import Del_fold
from components.move_fls import Move_fls
from components.settings import Settings
from PIL import Image, ImageTk

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
                                                 variable=segment_button_var,
                                                 command=self.switch_screen)
        self.segment_button.pack(side=LEFT, expand=1, padx=(100,0), pady=(10,0))
        self.selection.pack(fill=BOTH)

        button_image = CTkImage(light_image=Image.open("images\settings_dark.png"), dark_image=Image.open("images\settings_light.png"), size=(24, 24))
        self.button_path_sel = CTkButton(self.selection,
                           text="",
                           image=button_image,
                           command=lambda: self.switch_screen("Settings"),
                           width=24,
                           height=24)
        self.button_path_sel.pack(side=LEFT, padx=50, pady=(10,0))

        #main program
        self.screen = Move_fls(self)

        #starting our application
        self.start_app()
    
    def switch_screen(self, choice):
        screen = choice
        if screen == "Move_files":
            self.screen.destroy()
            self.screen = Move_fls(self)
        if screen == "Delete_folders":
            self.screen.destroy()
            self.screen = Del_fold(self)
        if screen == "Help":
            pass
        if screen == "Settings":
            self.screen.destroy()
            self.screen = Settings(self)

    def start_app(self):
        self.mainloop()

