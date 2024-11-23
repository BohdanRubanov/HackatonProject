# Импортируем кастом тк интер 
import customtkinter as ctk
# Класс создания фрейма
class Frame(ctk.CTkFrame):
    def __init__(self, master, width, height, border_width, **kwargs):
        super().__init__(master = master, width = width, height = height, border_width = border_width, **kwargs)
        button = ctk.CTkButton(
            master=self,  # Родительский элемент — текущий фрейм
            text="Нажми меня",  # Текст кнопки
            command=self.on_button_click  # Метод, который вызывается при нажатии
        )
        button.pack(pady=20, padx=20)  # Размещение кнопки в фрейме

   
