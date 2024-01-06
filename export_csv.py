import csv
import psycopg2

username = 'aklog_yan'
password = 'aBc'
database = 'db_lab3'
host = 'localhost'
port = '5432'

# Підключення до бази даних
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

# Експорт даних із таблиці Category
cur.execute('SELECT * FROM Category')
category_data = cur.fetchall()
with open('category_export.csv', 'w', encoding='utf-8', newline='') as category_file:
    category_writer = csv.writer(category_file)
    category_writer.writerow(['category_name'])
    category_writer.writerows(category_data)

# Експорт даних із таблиці Genre
cur.execute('SELECT * FROM Genre')
genre_data = cur.fetchall()
with open('genre_export.csv', 'w', encoding='utf-8', newline='') as genre_file:
    genre_writer = csv.writer(genre_file)
    genre_writer.writerow(['genre_type'])
    genre_writer.writerows(genre_data)

# Експорт даних із таблиці App
cur.execute('SELECT * FROM App')
app_data = cur.fetchall()
with open('app_export.csv', 'w', encoding='utf-8', newline='') as app_file:
    app_writer = csv.writer(app_file)
    app_writer.writerow(['app_name', 'category_name', 'app_size', 'app_content_rating', 'app_price'])
    app_writer.writerows(app_data)

# Експорт даних із таблиці App_Genre
cur.execute('SELECT * FROM App_Genre')
app_genre_data = cur.fetchall()
with open('app_genre_export.csv', 'w', encoding='utf-8', newline='') as app_genre_file:
    app_genre_writer = csv.writer(app_genre_file)
    app_genre_writer.writerow(['app_name', 'genre_type'])
    app_genre_writer.writerows(app_genre_data)

# Закриття з'єднання
conn.close()
