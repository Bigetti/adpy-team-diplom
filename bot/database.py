import psycopg2



def create_tables():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='Samsung555')
    cur = conn.cursor()

    # Определение таблицы пользователей
    cur.execute('''
        CREATE TABLE users (
            user_id BIGINT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            gender VARCHAR(10),
            age INTEGER,
            city VARCHAR(255),
            vk_id BIGINT,
            link VARCHAR(255),
            photos TEXT[]
        )
    ''')

    # Определение таблицы избранных
    cur.execute('''
        CREATE TABLE favorites (
            favorite_id SERIAL PRIMARY KEY,
            user_id BIGINT REFERENCES users(user_id),
            favorited_user_id BIGINT REFERENCES users(user_id),
            photo_urls TEXT[]  -- Список урлов фотографий
        )
    ''')

    # Определение таблицы черного списка
    cur.execute('''
        CREATE TABLE blacklist (
            blacklist_id SERIAL PRIMARY KEY,
            blocker_user_id BIGINT REFERENCES users(user_id),
            blocked_user_id BIGINT REFERENCES users(user_id)
        )
    ''')

    # Завершаем транзакцию и закрываем соединение
    conn.commit()
    cur.close()
    conn.close()


def add_user(user_data: dict) -> None:
    # ... код добавления пользователя ...
    pass

def add_user_to_group(user_id: int) -> None:
    # Логика добавления пользователя в базу данных при присоединении к группе
    pass

def add_user_to_black_list(user_id: int) -> None:
    # Логика добавления пользователя в базу данных при добавлении в избранное
    pass

def add_user_to_favorites(user_id: int) -> None:
    # Логика добавления пользователя в базу данных при добавлении в избранное
    pass

def get_favorites() -> list:
    # ... код получения списка избранных ...
    pass

# Вызываем функцию создания таблиц при инициализации модуля
create_tables()
