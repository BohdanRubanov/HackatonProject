import customtkinter as ctk

APP_WIDTH = 1280
APP_HEIGHT = 832
# Клас настройки окна и характеристик фрейма
class App(ctk.CTk):
    def __init__(self, fg_color):
        super().__init__(fg_color)
        self.APP_WIDTH = APP_WIDTH
        self.APP_HEIGHT = APP_HEIGHT
        self.X = 200
        self.Y = 200
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.resizable(False,False)
        self.title("makaki")
# Создаем окно и задаем ему цвет 
app = App(fg_color = "white")