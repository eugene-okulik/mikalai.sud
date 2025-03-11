# на всякий случай(безопасность наш конЁк))
# .env
# DB_USER='st-onl'
# DB_PASSW='AVNS_tegPDkI5BlB2lW5eASC'
# DB_HOST='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com'
# DB_PORT='25060'
# DB_NAME='st-onl'


import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()

base_path = os.path.dirname(__file__)
hw_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(hw_path, 'eugene_okulik', 'Lesson_16', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

for row in data:
    last_name, name, city = row['last'], row['Name'], row['city']

    query = "SELECT * FROM students WHERE name = %s"
    cursor.execute(query, (name,))

    result = cursor.fetchone()

    if result:
        print(f"Пользователь {name} найден в базе данных.")
    else:
        print(f"Пользователь {name} не найден в базе данных.")

cursor.close()
db.close()
