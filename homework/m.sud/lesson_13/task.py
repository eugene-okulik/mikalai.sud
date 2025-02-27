import os
import datetime

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(data_file_path)

with open(data_file_path) as q:
    print(q.read())
    with open(data_file_path) as file:
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        line3 = file.readline().strip()


def split_data(line):
    return line[3:29]


line1_data = split_data(line1)
line2_data = split_data(line2)
line3_data = split_data(line3)

print()

date1 = datetime.datetime.strptime(line1_data, "%Y-%m-%d %H:%M:%S.%f")
date2 = datetime.datetime.strptime(line2_data, "%Y-%m-%d %H:%M:%S.%f")
date3 = datetime.datetime.strptime(line3_data, "%Y-%m-%d %H:%M:%S.%f")

new_date1 = date1 + datetime.timedelta(weeks=1)
print(f"1) + 1 неделя: {new_date1}")

new_date2 = date2.strftime("%A")
print(f"2) день недели: {new_date2}")

time_now = datetime.datetime.now()
new_date3 = (time_now - date3).days
print(f"3) дней назад: {new_date3}")
