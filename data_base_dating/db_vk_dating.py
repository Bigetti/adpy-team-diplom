import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import sqlalchemy as sq
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from vk_api import VkApi


DSN = 'postgresql://postgres:mivida1@localhost:5432/dating'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_user_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String(50), nullable=False)
    last_name = sq.Column(sq.String(50))
    age = sq.Column(sq.Integer)
    gender = sq.Column(sq.Integer)
    city = sq.Column(sq.String(50))
    profile_link = sq.Column(sq.String(255))

    def __init__(self, id: int, vk_user_id: int, first_name: str, last_name: str, age: int, gender: int, city: dict, profile_link: str):
        self.id = id
        self.vk_user_id = vk_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.city = city['title']
        self.profile_link = profile_link



def add_user(session, user_id, vk_user_id, first_name, last_name, age, gender, city, profile_link):
    new_user = User(
        id=user_id,
        vk_user_id=vk_user_id,
        first_name=first_name,
        last_name=last_name,
        age=age,
        gender=gender,
        city=city['title'],
        profile_link=profile_link
        )
    session.add(new_user)
    session.commit()


def user_in_group(api, group_id, user_id):
    result = api.groups.isMember(group_id=group_id, user_id=user_id)
    return result.get('member', 0) == 1

    # Функция для авторизации в VK


def auth_vk_with_token(access_token, api_version='5.131'):
    vk_session = VkApi(token=access_token)
    return vk_session.get_api(), vk_session

    # Функция для получения данных пользователя из VK


def get_vk_user_info(api, user_id):
    user_info = api.users.get(user_ids=user_id, fields=['id', 'first_name', 'last_name', 'bdate', 'city', 'sex'])[0]
    return user_info

    # Функция для заполнения базы данных данными из VK


def fill_database_from_vk(session, api, vk_user_id, group_id):
    # Проверяем, состоит ли пользователь в группе
    if user_in_group(api, group_id, vk_user_id):
        # Если пользователь состоит в группе, получаем его информацию
        user_info = get_vk_user_info(api, vk_user_id)

        # Извлекаем нужные данные из user_info
        user_id = user_info['id']
        first_name = user_info['first_name']
        last_name = user_info['last_name']
        age = 2023 - int(user_info.get('bdate', '2023-01-01').split('.')[-1])  # Пример расчета возраста
        gender = user_info['sex']
        city = {'title': user_info.get('city', {}).get('title', 'Unknown')}
        profile_link = f'https://vk.com/id{user_id}'

        # Добавляем пользователя в базу данных
        add_user(session, user_id, vk_user_id, first_name, last_name, age, gender, city, profile_link)

class Favorite(Base):
    __tablename__ = 'favorites'

    id = sq.Column(sq.Integer, primary_key=True)
    top_photos = sq.Column(sq.String(400))
    id_user = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)

    user = sqlalchemy.orm.relationship('User', backref='favorites')

    def __init__(self, id: int, top_photos: str, id_user: int):
        self.id = id
        self.top_photos = top_photos
        self.id_user = id_user


class Blacklist(Base):
    __tablename__ = 'blacklist'

    id = sq.Column(sq.Integer, primary_key=True)
    top_photos = sq.Column(sq.String(400))
    id_user = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)

    user = sqlalchemy.orm.relationship('User', backref='blacklist')

    def __init__(self, id: int, top_photos: str, id_user: int):
        self.id = id
        self.top_photos = top_photos
        self.id_user = id_user


def drop_tables(engine):
    Base.metadata.drop_all(engine)


def create_table(engine):
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    drop_tables(engine)
    create_table(engine)
