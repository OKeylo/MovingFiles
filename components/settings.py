from customtkinter import *

class Settings(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, corner_radius=0)

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
