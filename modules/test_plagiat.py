# import nltk
# nltk.download('reuters')

# from nltk.corpus import reuters
# # print(reuters.fileids())  # Список доступных новостей и статей
# text = reuters.raw('test/14826')  # Чтение текста из одной из статей
# print(text)  # Печать первых 500 символов





# import wikipediaapi




# wiki_wiki = wikipediaapi.Wikipedia('HackatonProject (bgbg78915@gmail.com)', 'uk')



# page = wiki_wiki.page("Мавпи")

# print(page.text)
# import spacy

# # Загрузка модели (необходимо установить: pip install spacy)
# nlp = spacy.load("en_core_web_sm")

# def check_plagiarism_spacy(text1, text2):
#     doc1 = nlp(text1)
#     doc2 = nlp(text2)
#     return doc1.similarity(doc2)

# # Пример
# text1 = "This is a sample text for plagiarism checking."
# text2 = "Checking plagiarism using another sample text."
# similarity = check_plagiarism_spacy(text1, text2)
# print(f"Семантическое сходство: {similarity:.2f}")

from difflib import SequenceMatcher

my_str = ''
my_str2 = ''

match = SequenceMatcher(None, my_str, my_str2)

result = match.ratio() * 100

print(f'Процент плагиата: {result:.2f}%')

