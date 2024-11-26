#Импорт кастом тк интера
import customtkinter as ctk
from modules.button_creation import CustomButton
from modules.label_creation import CustomLabel
from modules.new_windows import ToplevelWindow
from PIL import Image, ImageTk
from tkinter import filedialog
from docx import Document
import PyPDF2
from modules.ai import client

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
        
        self.main_frame = ctk.CTkFrame(self, fg_color="#7593EB")
        self.main_frame.pack(fill="both", expand=True)
         # Загрузка изображения для кнопки
         
        
        self.button1 = CustomButton(self.main_frame, command = self.new_window_with_text, text="TEXT")
        self.button1.place(x= 530, y=670)
        
        
        self.button2 = CustomButton(self.main_frame, text="FILE", command = self.new_window_with_file)
        self.button2.place(x= 770, y=670)

         
        self.button3 = CustomButton(self.main_frame, text="IMAGE", command = self.new_window_with_image)
        self.button3.place(x= 1010, y=670)
        
 

        self.bg_image = Image.open("modules\\images\\new_menu_frame.png")
        self.bg_image= self.bg_image.resize((self.winfo_width(), self.winfo_height()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # self.label1 = CustomLabel(self, image = self.bg_photo, text="")
        # self.label1.place(relx=0, rely=0, relwidth = 1, relheight =1)
        
        canvas = ctk.CTkCanvas(self.main_frame, width=600, height=400, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # self.attributes("-transparentcolor", "white")
        
        # Полнимаем кнопки
        self.button1.lift()
        self.button2.lift()
        self.button3.lift()
    def new_window_with_text(self):
            
            self.toplevel_window_with_text = ToplevelWindow(self) 
            self.toplevel_window_with_text.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
            self.withdraw()
            
            self.button_image_start= ctk.CTkImage(Image.open("modules\\images\\button_start.png"), size=(282, 64))
            self.button_start = CustomButton(self.toplevel_window_with_text, image= self.button_image_start)
            self.button_start.place(x = 499, y=666)
            
            self.input_text_window= ctk.CTkImage(Image.open("modules\\images\\text_input.png"), size=(451, 516))
            self.input_text = ctk.CTkEntry(self.toplevel_window_with_text, width=451, height= 516, fg_color="#D4DEE6", text_color="black", placeholder_text_color="#000000")
            self.input_text.place(x = 414, y=30)

            self.image_back= ctk.CTkImage(Image.open("modules\\images\\background_image_for_second_frame.png"), size= (1280, 832))
            #путь к фрей
            self.label_image= ctk.CTkLabel(self.toplevel_window_with_text, image= self.image_back, text="")
            self.label_image.place(x= 0, y=0)
            
            self.button_start.lift()
            self.input_text.lift()
            

            
            
            

    def new_window_with_image(self):
        self.toplevel_window_with_image = ToplevelWindow(self, width= 451, height= 516) 
        self.toplevel_window_with_image.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.withdraw()
        
        self.button_image_start2= ctk.CTkImage(Image.open("modules\\images\\button_start.png"), size=(282, 64))
        self.button_start2 = CustomButton(self.toplevel_window_with_image, image= self.button_image_start2)
        self.button_start2.place(x = 499, y=666)
  
        self.input_text_window2= ctk.CTkImage(Image.open("modules\\images\\text_input.png"), size=(451, 516))
        self.input_text2 = ctk.CTkEntry(self.toplevel_window_with_image, width=451, height= 516, fg_color="#D4DEE6")
        self.input_text2.place(x = 415.5, y=80)
        
        self.image_back2= ctk.CTkImage(Image.open("modules\\images\\background_image_for_second_frame.png"), size= (1280, 832))
        self.label_image= ctk.CTkLabel(self.toplevel_window_with_image, image= self.image_back2, text="")
        self.label_image.place(x= 0, y=0)
        
        self.upload_button2=CustomButton(self.toplevel_window_with_image, fg_color="#D4DEE6", command=self.load_image )
        self.upload_button2.place(x = 415.5, y=80)
        
        self.button_start2.lift()
        self.input_text2.lift()
        self.upload_button2.lift()
    def load_image(self):
        image_path = filedialog.askopenfilename(
        title="Выберите фото",
        filetypes=[("Image", "*.png"), ("All Files", "*.*")])
        if image_path:
            try:
                image = Image.open(image_path)
                self.input_text_window2 = ctk.CTkImage(image, size=(451, 516))
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
        self.input_text2 = ctk.CTkLabel(self.toplevel_window_with_image, image=self.input_text_window2, text="")
        self.input_text2.place(x=414.5, y=85)

    def new_window_with_file(self):
        self.toplevel_window_with_file = ToplevelWindow(self) 
        self.toplevel_window_with_file.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.withdraw()
        self.button_image_start3= ctk.CTkImage(Image.open("modules\\images\\button_start.png"), size=(282, 64))
        self.button_start3 = CustomButton(self.toplevel_window_with_file, image= self.button_image_start3, command=self.new_window_with_result )
        self.button_start3.place(x = 499, y=666)

        
        self.input_text3 = ctk.CTkTextbox(self.toplevel_window_with_file, width=451, height=516, fg_color="#D4DEE6", text_color="black", wrap="word")
        self.input_text3.place(x = 414, y=30)
        
        self.upload_button=CustomButton(self.toplevel_window_with_file,text="+",width=50, height=50, fg_color="#D4DEE6", command=self.load_file )
        self.upload_button.place(x=390, y=680)
    def load_file(self):
            file_path = filedialog.askopenfilename(title="Выберите файл",filetypes=[("Text Files", "*.txt"),("PDF Files", "*.pdf"), ("Word Documents", "*.docx"), ("All Files", "*.*")])
            if file_path:
                try:
                    if file_path.endswith(".txt"):
                        # Чтение текстового файла
                        with open(file_path, "r", encoding="utf-8") as file:
                            self.content = file.read()
                    elif file_path.endswith(".docx"):
                        # Чтение Word-документа
                        doc = Document(file_path)
                        self.content = "\n".join([para.text for para in doc.paragraphs])
                    elif file_path.endswith(".pdf"):
                
                        with open(file_path, "rb") as file:
                            reader = PyPDF2.PdfReader(file)
                            self.content = ""
                            for page in reader.pages:
                                self.content += page.extract_text()
                    else:
                        print("Неподдерживаемый формат файла")
                        return

                    # Очистка и вставка текста в input_text3
                    self.input_text3.delete("1.0", "end")  # Очистить текстовое поле
                    self.input_text3.insert("1.0", self.content)  # Вставить текст

                except Exception as e:
                    print(f"Ошибка при чтении файла: {e}")
    def new_window_with_result(self):
        self.toplevel_window_with_result = ToplevelWindow(self) 
        self.toplevel_window_with_result.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")                 
        self.toplevel_window_with_file.withdraw()
        
        
        self.image_back_result= ctk.CTkImage(Image.open("modules\\images\\result.png"), size= (1280, 832))
        self.label1_image_result=ctk.CTkLabel(self.toplevel_window_with_result, image= self.image_back_result, text="" )
        self.label1_image_result.place(x = 0, y=0)
        
        # self.input_text_result1= ctk.CTkImage(Image.open("modules\\images\\text_input.png"), size=(451, 516))
        # self.input_text_result = ctk.CTkEntry(self.toplevel_window_with_result, width=451, height= 516, fg_color="#D4DEE6", text_color="black")
        # self.input_text_result.place(x = 415.5, y=80)
        
        
        self.result_for_file = ctk.CTkLabel(self.toplevel_window_with_result, text= self.content, fg_color="white", text_color= "black")
        self.result_for_file.place(x = 415.5, y=80)
        
        # self.input_text_result.lift()
        # self.result_for_file.lift()
        
        
        

   

       
       

# Создаем окно и задаем ему цвет 
app = App(fg_color = "white")
