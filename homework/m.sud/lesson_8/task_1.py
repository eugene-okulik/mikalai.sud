# Задание 1
# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary. А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

if_bonus = random.choice([True, False])
bonus = random.randint(1, 100)
print("Input salary:")
salary_input = int(input())
bb = str(if_bonus)
if if_bonus:
    print("Great! you have bonus: " + bb + ". Your salary is: " + str(salary_input + bonus))
else:
    print("._. not bonus: your salary is: " + str(salary_input))
