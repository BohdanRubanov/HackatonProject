import customtkinter as ctk

def create_label(parent, text="Label", width=200, height=50, text_color=None, font=("Arial", 16, "bold"), anchor="e"):
    return ctk.CTkLabel(master=parent, text=text, width=width, height=height, text_color=text_color, font=font, anchor=anchor)