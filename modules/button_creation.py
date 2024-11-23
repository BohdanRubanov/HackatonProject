import customtkinter as ctk
class CustomButton(ctk.CTkButton):
    def __init__(self, parent, text="", width=200, height=50, image=None, fg_color="transparent", hover = False, **kwargs) :
        super().__init__( master=parent,
                         text=text, 
                         width=width,
                         height=height, 
                         image=image, 
                         hover=hover,
                         fg_color=fg_color, 
                         border_width=0,
                         **kwargs)