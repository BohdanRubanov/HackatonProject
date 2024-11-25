import customtkinter as ctk
class CustomLabel(ctk.CTkLabel):
    def __init__(parent,*args,  **kwargs):
        super().__init__( *args,**kwargs)