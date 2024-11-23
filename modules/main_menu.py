#Импорт кастом тк интера
import customtkinter as ctk
from modules.button_creation import create_button
from modules.label_creation import create_label

# Создание констант с размерами окна
APP_WIDTH = 1280
APP_HEIGHT = 832
# Клас настройки окна 
class App(ctk.CTk):
    # метод конструктор для класса
    def __init__(self, fg_color):
        # Получаем свойство цвета заднего фона
        super().__init__(fg_color)
        # Свойства для размера окна и его расположения
        self.APP_WIDTH = APP_WIDTH
        self.APP_HEIGHT = APP_HEIGHT
        self.X = 200
        self.Y = 0
        # Задаем размеры окна и его расположение
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        # Говорим что нельзя менять размер окна
        self.resizable(False,False)
        # Указываем название окна
        self.title("makaki")
        # Создаем кнопки
        self.button1 = create_button(self, text="TEXT", width=200, height=50)
        self.button1.place(x= 500, y=700)
        self.button2 = create_button(self, text="FILE", width=200, height=50)
        self.button2.place(x= 750, y=700)
        self.button3 = create_button(self, text="IMAGE", width=200, height=50)
        self.button3.place(x= 1000, y=700)
        # Создаем надписи
        self.label1 = create_label(self, text="CHOOSE FORMAT", width=300, height=50,  text_color="black", font=("Arial", 28))
        self.label1.place(x=700, y=600)
        self.label2 = create_label(self, text="  Monkey \nAgainstPlag", width=300, height=50,  text_color="black", font=("Arial", 72, "bold"))
        self.label2.place(x=700, y=50)
        self.label3 = create_label(self, text="Are you a teacher and want to check\nyour student`s work for plagiarism?\nSo this app is for you! In a couple\nof clicks, our program will check the\nstudent`s work and give you an answer.", width=300, height=50,  text_color="black", font=("Arial", 24), anchor="e")
        self.label3.place(x=700, y=300)
       

# Создаем окно и задаем ему цвет 
app = App(fg_color = "white")
