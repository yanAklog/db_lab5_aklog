import csv
import psycopg2
import random


username = 'aklog_yan'
password = 'aBc'
database = 'db_lab3'
host = 'localhost'
port = '5432'


csv_file_path = 'googleplaystore.csv'


random.seed(42)

# Підключення до бази даних
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

# Очищення таблиць перед імпортом
cur.execute('DELETE FROM App_Genre;')
cur.execute('DELETE FROM App;')
cur.execute('DELETE FROM Genre;')
cur.execute('DELETE FROM Category;')

# Фіксація змін
conn.commit()

# Відкриття CSV-файлу та читання унікальних значень "Category"
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    categories = set(row['Category'] for row in reader)

# Вставка унікальних значень "Category" в таблицю Category
for category in categories:
    cur.execute("""
        INSERT INTO Category (category_name)
        VALUES (%s)
        ON CONFLICT (category_name) DO NOTHING
    """, (category,))

# Фіксація змін
conn.commit()

# Відкриття CSV-файлу та читання унікальних значень "Genre"
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Множина для відслідковування унікальних значень "Genre"
    unique_genres = set()
    
    # Розділення й додавання унікальних значень "Genre" у множину
    for row in reader:
        genres = row['Genres'].split(';')
        for genre in genres:
            unique_genres.add(genre.strip())

# Вставка унікальних значень "Genre" у таблицю Genre
for genre in unique_genres:
    cur.execute("""
        INSERT INTO Genre (genre_type)
        VALUES (%s)
        ON CONFLICT (genre_type) DO NOTHING
    """, (genre,))

# Фіксація змін
conn.commit()

# Відкриття CSV-файла й читання перших 125 значений "App", "Category", (випадково згенерованого) "Size", "Content Rating" і (випадково згенерованого) "prod_price"
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Множина для відслідковування унікальних значень "App"
    unique_apps = set()

    apps_data = [
        (
            row['App'],
            row['Category'],
            random.randint(5, 50),  # Випадкове значення для "app_size"
            row['Content Rating'],
            round(random.uniform(0, 5), 2)  # Випадкове значення для "prod_price"
        )
        for row in reader if len(unique_apps) < 125 and (row['App'] not in unique_apps and unique_apps.add(row['App']) is None)
    ]

# Вставлення перших 125 записей у таблицю App
cur.executemany("""
    INSERT INTO App (app_name, category_name, app_size, app_content_rating, app_price)
    VALUES (%s, %s, %s, %s, %s)
""", apps_data)

# Фіксація змін
conn.commit()

# Відкриття CSV-файла й читання перших 125 значений "App" и "Genres" для вставки в таблицю App_Genre
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # Множина для відслідковування уікальних значень "App"
    unique_apps = set()

    app_genre_data = [
        (
            row['App'],
            genre.strip()  # Жанри розділені, застосовуємо strip() для видалення зайвих пробілів
        )
        for row in reader if len(unique_apps) < 125 and (row['App'] not in unique_apps and unique_apps.add(row['App']) is None)
        for genre in row['Genres'].split(';')
    ]

# Вставка перших 125 записів у таблицу App_Genre
cur.executemany("""
    INSERT INTO App_Genre (app_name, genre_type)
    VALUES (%s, %s)
""", app_genre_data)

# Фиксація змін
conn.commit()



# Закриття з'єднання
conn.close()











