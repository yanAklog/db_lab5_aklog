import json
import decimal
import psycopg2
from psycopg2.extras import RealDictCursor

# Визначення функції для перетворення Decimal в float при серіалізації у JSON
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

username = 'aklog_yan'
password = 'aBc'
database = 'db_lab3'
host = 'localhost'
port = '5432'

# Підключення до бази даних
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor(cursor_factory=RealDictCursor)

# Функція для отримання даних із таблиці
def get_table_data(table_name):
    cur.execute(f'SELECT * FROM {table_name}')
    return cur.fetchall()

# Отримання даних із кожної таблиці
category_data = get_table_data('Category')
genre_data = get_table_data('Genre')
app_data = get_table_data('App')
app_genre_data = get_table_data('App_Genre')

# Об'єднання даних у один словник
all_data = {
    'Category': category_data,
    'Genre': genre_data,
    'App': app_data,
    'App_Genre': app_genre_data,
}

# Закриття з'єднання
conn.close()

# Збереження даних у один JSON-файл з використанням параметра default
with open('all_data_export.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=2, default=decimal_default)

