import customtkinter as ctk
def create_button(parent, text="Button", width = 200, height =50):
    return ctk.CTkButton(master=parent, text=text, width=width, height=height)