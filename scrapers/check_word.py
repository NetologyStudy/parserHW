import re


def contains_any_word(text, word_list):
    """Данная функция ищет совпадение слова, например: 'дизайн' и 'дизайнер' пройдет проверку"""

    return any(word in text for word in word_list)


def contains_any_word_reg(text, word_list):
    """Данная функция ищет точное совпадение слов"""

    pattern = r'\b(' + '|'.join(re.escape(word) for word in word_list) + r')\b'
    return bool(re.search(pattern, text, re.IGNORECASE))