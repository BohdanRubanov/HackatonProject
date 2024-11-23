import customtkinter as ctk
def create_button(parent, text="",   image=None):
    return ctk.CTkButton(master=parent, text=text,   image=image)