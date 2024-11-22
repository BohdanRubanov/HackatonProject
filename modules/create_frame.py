import customtkinter as ctk
# Класс создания фрейма
class Frame(ctk.CTkFrame):
    def __init__(self, master, width, height, border_width, **kwargs):
        super().__init__(master = master, width = width, height = height, border_width = border_width, **kwargs)
        
