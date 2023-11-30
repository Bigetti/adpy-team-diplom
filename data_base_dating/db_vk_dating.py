import sqlalchemy as sq
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


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


class Favorit(Base):
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
