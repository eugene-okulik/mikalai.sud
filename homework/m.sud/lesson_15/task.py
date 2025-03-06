import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True, buffered=True)

create_student = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
cursor.execute(create_student, ('st_name_v123', 'st_second_name_v123'))
student_id = cursor.lastrowid

add_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    add_books,
    [
        ('book_v123', f'{student_id}'),
        ('taken_book_v123', f'{student_id}')
    ]
)

create_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
cursor.execute(create_group, ('title_groups_v123', 'start_v123', 'end_v123'))
group_id = cursor.lastrowid

student_update = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(student_update, (f'{group_id}', f'{student_id}'))

create_subject = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(create_subject, ('subject_v123',))
subject1_id = cursor.lastrowid
cursor.execute(create_subject, ('subject_v321',))
subject2_id = cursor.lastrowid

create_lesson = 'INSERT INTO lessons (title, subject_id) VALUES (%s,%s)'
cursor.execute(create_lesson, ('les_1', f'{subject1_id}'))
lesson1_id = cursor.lastrowid
cursor.execute(create_lesson, ('les_2', f'{subject1_id}'))
lesson2_id = cursor.lastrowid
cursor.execute(create_lesson, ('les_3', f'{subject2_id}'))
lesson3_id = cursor.lastrowid
cursor.execute(create_lesson, ('les_4', f'{subject2_id}'))
lesson4_id = cursor.lastrowid

create_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s,%s,%s)'
cursor.executemany(
    create_marks,
    [
        (1, f'{lesson1_id}', f'{student_id}'),
        (2, f'{lesson2_id}', f'{student_id} '),
        (3, f'{lesson3_id}', f'{student_id} '),
        (4, f'{lesson4_id}', f'{student_id} ')
    ]
)
db.commit()

cursor.execute(f'SELECT * FROM marks m WHERE student_id = {student_id}')
print(cursor.fetchall())
cursor.execute(f'SELECT * FROM books b WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

cursor = db.cursor(dictionary=True)
query = f"""
SELECT s.name, s.second_name, s.group_id,books.title as book_title,  g.title as group_title,
g.start_date, g.end_date, subjets.title as subject_title, l.title as lesson_title, m2.value
FROM books
join students s on books.taken_by_student_id = s.id
join marks m2 on m2.student_id = s.id
join `groups` g on s.group_id = g.id
join lessons l on m2.lesson_id = l.id
join subjets on l.subject_id = subjets.id
WHERE s.id = {student_id}
"""
cursor.execute(query)
student_data_table = cursor.fetchall()
for i in student_data_table:
    print(i)

db.close()
