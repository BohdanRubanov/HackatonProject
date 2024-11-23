import customtkinter as ctk
class CustomLabel(ctk.CTkLabel):
    def __init__(parent, text="", width=200, height=50, text_color=None, font=("Arial", 16, "bold"),  **kwargs):
        super().__init__(  master=parent,
            text=text,
            width=width,
            height=height,
            text_color=text_color,
            font=font,
            **kwargs)