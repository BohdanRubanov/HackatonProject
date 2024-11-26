from sklearn.feature_extraction.text import CountVectorizer 


def calculate_lexical_diversity(text):
    """Вычисление лексического разнообразия."""
    vectorizer = CountVectorizer()
    tokens = vectorizer.fit_transform([text]).toarray()
    unique_words = tokens.sum(axis=0).nonzero()[0].size
    total_words = tokens.sum()
    return unique_words / total_words if total_words > 0 else 0

def assess_text_originality(text):
    """Оценка оригинальности текста на основе лексического разнообразия."""
    diversity = calculate_lexical_diversity(text)

    if diversity < 0.3:
        return f"Лексическое разнообразие: {diversity:.2f}. Текст неоригинальный: много повторений."
    elif 0.3 <= diversity <= 0.7:
        return f"Лексическое разнообразие: {diversity:.2f}. Текст умеренно оригинальный."
    elif 0.7 < diversity < 1.0:
        return f"Лексическое разнообразие: {diversity:.2f}. Текст высокооригинальный."
    elif diversity == 1.0:
        return f"Лексическое разнообразие: {diversity:.2f}. Текст подозрительно исскуственный"

# print(assess_text_originality("Научно-технический прогресс оказывает значительное влияние на жизнь современного общества. С одной стороны, инновации облегчают повседневные задачи, но с другой — вызывают ряд этических и социальных вопросов. Например, использование искусственного интеллекта становится все более распространенным, что требует создания новых правовых рамок для регулирования этой области."))