# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
#
# Преобразуйте эту дату в питоновский формат, после этого:
#
# 1. Распечатайте полное название месяца из этой даты
#
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"


import datetime

input_data = "Jan 15, 2023 - 12:05:33"

py_date = datetime.datetime.strptime(input_data, "%b %d, %Y - %H:%M:%S")

print(py_date.strftime("%B"))
print(py_date.strftime("%d.%m.%Y, %H:%M"))
