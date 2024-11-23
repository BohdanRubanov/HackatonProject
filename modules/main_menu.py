#Импорт кастом тк интера
import customtkinter as ctk
from modules.button_creation import CustomButton
from modules.label_creation import CustomLabel
from PIL import Image, ImageTk

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
         # Загрузка изображения для кнопки
        self.button1 = CustomButton(self, text="", fg_color= "transparent", hover = False)
        self.button1.place(x= 530, y=670)

        self.button2 = CustomButton(self, text="",  fg_color= "transparent", hover = False)
        self.button2.place(x= 770, y=670)

        self.button3 = CustomButton(self, text="",  fg_color= "transparent", hover = False)
        self.button3.place(x= 1010, y=670)

        
        self.bg_image = Image.open("modules\\images\\Background.png")
        self.bg_image= self.bg_image.resize((self.winfo_width(), self.winfo_height()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.label1 = CustomLabel(self, image = self.bg_photo)
        self.label1.place(relx=0, rely=0, relwidth = 1, relheight =1)

        # Полнимаем кнопки
        self.button1.lift()
        self.button2.lift()
        self.button3.lift()

       
       

# Создаем окно и задаем ему цвет 
app = App(fg_color = "white")
