# Задание 3
# Даны такие списки:
#
# students = ['Ivanov', 'Petrov', 'Sidorov']
#
# subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

student1, student2, student3 = students
subject1, subject2, subject3 = subjects

my_text = f'Students: {student1}, {student2}, {student3} study these subjects: {subject1}, {subject2}, {subject3}.'
print(my_text)
