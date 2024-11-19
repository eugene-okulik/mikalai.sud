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

print("Students: " + student1 + ", " + student2 + ", " + student3 + " " + "study these subjects:",
      subject1 + ", " + subject2 + ", " + subject3 + ".")

my_text1 = "Students: %s, %s, %s study these subjects: %s, %s, %s."
print(my_text1 % (student1, student2, student3, subject1, subject2, subject3))

my_text2 = "Students: {}, {}, {} study these subjects: {}, {}, {}."
print(my_text2.format(student1, student2, student3, subject1, subject2, subject3))

my_text3 = "Students: {2}, {1}, {0} study these subjects: {4}, {3}, {5}."
print(my_text3.format(student3, student2, student1, subject2, subject1, subject3))

print("Students:", ", ".join(students) + " study these subhects:", ", ".join(subjects) + ".")
