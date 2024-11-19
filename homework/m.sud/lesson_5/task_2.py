# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
#
# результат операции: 42
#
# результат операции: 514
#
# результат работы программы: 9
#
# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.

default_number = 10

result1 = "результат операции: 42"
slice1_index = (result1.index(":"))
# +2 чтобы обрезать пробел и двуеточие, ох, как же я намучался с этими слайсами в го)
print(result1[slice1_index + 2:])  # получаем число после двуеточия
r1_number = int(result1[slice1_index + 2:])  # преобразуем в инт и засовываем в переменную
print(r1_number + default_number)  # число +10

result2 = "результат операции: 514"
slice2_index = (result2.index(":"))
print(result2[slice2_index + 2:])
r2_number = int(result2[slice2_index + 2:])
print(r2_number + default_number)

result3 = "результат работы программы: 9"
slice3_index = (result3.index(":"))
print(result3[slice3_index + 2:])
r3_number = int(result3[slice3_index + 2:])
print(r3_number + default_number)

print(r1_number + r2_number + r3_number)  # суммирование всех чисел
