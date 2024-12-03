# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
#
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

def f_gen():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = f_gen()

num3 = 1
num200 = 1
num1000 = 1
num100000 = 1

for i, number in enumerate(fib_gen):
    if i == 4:
        num3 = number
    elif i == 199:
        num200 = number
    elif i == 999:
        num1000 = number
    elif i == 99999:
        num100000 = number
        break

print("1: " + str(num3))
print("200: " + str(num200))
print("1000: " + str(num1000))
print("100000: " + str(num100000))
