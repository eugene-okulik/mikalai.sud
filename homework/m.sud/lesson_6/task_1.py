# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте:
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после
# того же слова, но уже преобразованного.

text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
print(text)

new_text = text.split()
print(new_text)
final_text = []
for i in new_text:
    if i.endswith(","):
        word = i[:-1]
        word_final = word + "ing,"
        # print(word_final)
        final_text.append(word_final)
    elif i.endswith("."):
        word = i[:-1]
        word_final = word + "ing."
        # print(word_final)
        final_text.append(word_final)
    else:
        word = i + "ing"
    # print(word)
    final_text.append(word)

print(" ".join(final_text))
