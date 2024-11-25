import customtkinter as ctk
# import tkinter
class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text="", width=200, height=50, image=None, fg_color="#7593EB", hover = False, text_color="#090909", **kwargs) :
        super().__init__( master=parent,
                         text=text, 
                         width=width,
                         height=height, 
                         image=image, 
                         hover=hover,
                         fg_color=fg_color, 
                         text_color=text_color,
                         font=("Jura",32),
                         **kwargs)
