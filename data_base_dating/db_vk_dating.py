import sqlalchemy as sq
import sqlalchemy.orm
from sqlalchemy.orm import declarative_base


DSN = 'postgresql://postgres:mivida1@localhost:5432/dating'
engine = sq.create_engine(DSN)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    vk_user_id = sq.Column(sq.Integer, unique=True, index=True)
    first_name = sq.Column(sq.String(50), nullable=False)
    last_name = sq.Column(sq.String(50))
    age = sq.Column(sq.Integer)
    gender = sq.Column(sq.Integer)
    city = sq.Column(sq.String(50))
    profile_link = sq.Column(sq.String(255))

    def __init__(self, id: int, vk_user_id: int, first_name: str, last_name: str, age: int, gender: int, city: dict, profile_link: str):
        self.vk_user_id = vk_user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.city = city['title']
        self.profile_link = profile_link



class Favorite(Base):
    __tablename__ = 'favorites'

    id = sq.Column(sq.Integer, primary_key=True)
    added_user_id = sq.Column(sq.Integer, index=True)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False, index=True)

    sq.UniqueConstraint('added_user_id', 'id_user', name='uq_favorite_user_added_user_id')

    user = sqlalchemy.orm.relationship('User', backref='favorites')

    def __init__(self, id: int, added_user_id: int, id_user: int):
        self.added_user_id = added_user_id
        self.id_user = id_user


class Blacklist(Base):
    __tablename__ = 'blacklist'

    id = sq.Column(sq.Integer, primary_key=True)
    added_user_id = sq.Column(sq.Integer,index=True)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False, index=True)

    sq.UniqueConstraint('added_user_id', 'id_user', name='uq_blacklist_user_added_user_id')

    user = sqlalchemy.orm.relationship('User', backref='blacklist')

    def __init__(self, id: int, added_user_id: int, id_user: int):
        self.added_user_id = added_user_id
        self.id_user = id_user


def drop_tables(engine):
    Base.metadata.drop_all(engine)


def create_table(engine):
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    drop_tables(engine)
    create_table(engine)
