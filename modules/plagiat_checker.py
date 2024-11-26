from transformers import pipeline

# Модель для определения текста от ИИ
detector = pipeline("text-classification", model="roberta-base-openai-detector")
