import customtkinter as ctk
def create_button(parent, text="", width = 200, height =50,  image=None, fg_color="transparent",hover_color="transparent"):
    return ctk.CTkButton(master=parent, text=text, width=width, height=height,  image=image, fg_color=fg_color,hover_color=hover_color)