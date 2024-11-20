import string

# Исходный текст
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero."

# Разбиваем текст на слова
words = text.split()

# Список для сохранения изменённых слов
modified_words = []

# Проходим по каждому слову
for word in words:
    if word[-1] in string.punctuation:  # Если слово заканчивается на знак препинания
        modified_word = word[:-1] + 'ing' + word[-1]  # Добавляем 'ing' перед знаком препинания
    else:
        modified_word = word + 'ing'  # Добавляем 'ing', если знака препинания нет
    modified_words.append(modified_word)

# Собираем обратно текст из изменённых слов
modified_text = ' '.join(modified_words)

# Выводим результат
print(modified_text)
