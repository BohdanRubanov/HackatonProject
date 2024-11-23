import customtkinter as ctk
class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text="", width=200, height=50, fg_color=None, hover = False, **kwargs):
        super().__init__( master=parent, text=text, width=width,height=height, fg_color=fg_color, hover=hover, **kwargs)