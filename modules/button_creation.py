import customtkinter as ctk
def create_button(parent, text="", width = 200, height =50,  image=None):
    return ctk.CTkButton(master=parent, text=text, width=width, height=height,  image=image)