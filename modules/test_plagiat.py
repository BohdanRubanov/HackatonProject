# import nltk
# nltk.download('reuters')

# from nltk.corpus import reuters
# # print(reuters.fileids())  # Список доступных новостей и статей
# text = reuters.raw('test/14826')  # Чтение текста из одной из статей
# print(text)  # Печать первых 500 символов





import wikipediaapi
from difflib import SequenceMatcher

wiki_wiki = wikipediaapi.Wikipedia('HackatonProject (bgbg78915@gmail.com)', 'uk')

# page = wiki_wiki.page("Динозаври")

# print(page.text[:500])

# my_str = page.text[:500]
# my_str2 = 'Диноза́ври (Dinosauria — від дав.-гр. δεινός — «страшний» і σαῦρος — «ящір») — надряд завропсидів, який з’явився близько 251 млн років тому. Динозаври були панівною групою наземних хребетних у мезозойську еру (тріасовий, юрський і крейдовий періоди), аж до масового вимирання 65 млн років тому. Описано понад 1000 видів. Рештки знайдені на всіх сучасних континентах. Поділяються на 2 ряди: птахотазові (Ornithischia) і ящеротазові (Saurischia), останні були предками птахів. Птахи — єдина лінія динозаврів, яка, як відомо, пережила подію крейдяно-палеогенового вимирання. Довжина різних видів коливалася від 0,35 до 35 м, вага — від 110 грамів до понад 100 т.'

# match = SequenceMatcher(None, my_str, my_str2)

# result = match.ratio() * 100

# print(f'Процент плагиата: {result:.2f}%')


