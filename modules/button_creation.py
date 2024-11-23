import customtkinter as ctk
class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text="", width=200, height=50, image=None, fg_color="transparent", hover_color="white", **kwargs):
        super().__init__( master=parent, text=text, width=width,height=height, image=image, fg_color=fg_color, hover_color=hover_color, **kwargs)