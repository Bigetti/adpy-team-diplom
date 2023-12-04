import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from db_vk_dating import User

DSN = 'postgresql://postgres:mivida1@localhost:5432/dating'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()



def add_to_favorites(user_id, added_user_id):
    user = session.query(User).filter_by(vk_user_id=user_id).first()
    if user:
        user.add_to_favorites(added_user_id)


def add_to_blacklist(user_id, added_user_id):
    user = session.query(User).filter_by(vk_user_id=user_id).first()
    if user:
        user.add_to_blacklist(added_user_id)


def get_favorites(user_id):
    user = session.query(User).filter_by(vk_user_id=user_id).first()
    if user:
        return user.favorites


def get_blacklist(user_id):
    user = session.query(User).filter_by(vk_user_id=user_id).first()
    if user:
        return user.blacklist


def get_user_info(user_id):
    user = session.query(User).filter_by(vk_user_id=user_id).first()
    if user:
        return user


session.commit()
session.close()


