import psycopg2
import matplotlib.pyplot as plt

username = 'aklog_yan'
password = 'aBc'
database = 'db_lab3'
host = 'localhost'
port = '5432'


def create_or_replace_view(connection, view_name, view_definition):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE OR REPLACE VIEW {view_name} AS {view_definition};")


def execute_and_visualize_view(connection, view, visualization_type):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {view};")
        data = cursor.fetchall()

        if visualization_type == "bar":
            labels, values = zip(*data)
            plt.bar(labels, values)
            plt.xlabel('Категорії' if "AppCountByCategory" in view else 'Типи жанрів' if "GenrePercentage" in view else 'Категорії')
            plt.ylabel('Кількість застосунків' if "AppCountByCategory" in view else 'Відсоткове співвідношення' if "GenrePercentage" in view else 'Середній розмір застосунків (МБ)')
            plt.title(f'VIEW: {view}')
            plt.show()

        elif visualization_type == "pie":
            labels, percentages = zip(*data)
            plt.pie(percentages, labels=labels, autopct='%1.1f%%')
            plt.title(f'VIEW: {view}')
            plt.show()

        elif visualization_type == "plot":
            labels, avg_sizes = zip(*data)
            plt.plot(labels, avg_sizes, marker='o')
            plt.xlabel('Категорії')
            plt.ylabel('Середній розмір застосунків (МБ)')
            plt.title(f'VIEW: {view}')
            plt.show()

if __name__ == "__main__":
    try:
        connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

        # Створення чи заміна VIEW
        create_or_replace_view(connection, "AppCountByCategory", "SELECT category_name, COUNT(*) as app_count FROM App GROUP BY category_name;")
        create_or_replace_view(connection, "GenrePercentage", "SELECT genre_type, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM App_Genre) AS genre_percentage FROM App_Genre GROUP BY genre_type;")
        create_or_replace_view(connection, "AvgAppSizeByCategory", "SELECT category_name, AVG(app_size) as avg_app_size FROM App GROUP BY category_name;")

        # Коміт транзакції
        connection.commit()

        # Візуалізація результатів для кожного VIEW
        execute_and_visualize_view(connection, "AppCountByCategory", "bar")
        execute_and_visualize_view(connection, "GenrePercentage", "pie")
        execute_and_visualize_view(connection, "AvgAppSizeByCategory", "plot")

    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        if connection:
            connection.close()
