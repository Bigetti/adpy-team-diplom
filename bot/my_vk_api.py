import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random


class VKApi:

    def __init__(self, group_token, group_id):
        self.vk = vk_api.VkApi(token=group_token)
        self.group_id = group_id
        self.longpoll = VkBotLongPoll(self.vk, self.group_id)
        self.user_data = {}  # Добавляем эту строку, чтобы инициализировать атрибут

    def save_user_info(self, user_id, user_info):
        self.user_data[user_id] = user_info

    def get_user_info(self, user_id):
        return self.user_data.get(user_id, {})

    def search_users(self, city_id, age_from, age_to, gender, user_id):
        try:
            user_info = self.get_user_info(user_id)
            if not user_info:
                print(f'No user information found for user {user_id}')
                return None

            search_result = self.vk.method('users.search', {
                'count': 3,
                'city': user_info.get('city_id', city_id),
                'age_from': user_info.get('age_from', age_from),
                'age_to': user_info.get('age_to', age_to),
                'sex': user_info.get('gender', gender),
                'has_photo': 1,
                'fields': "photo_max_orig,screen_name",
            })

            return search_result['items']

        except vk_api.exceptions.ApiError as e:
            print(f'Error during user search: {e}')
            return None


    # def get_top_photos(self, user_id):
    #     """
    #     Метод для получения трех самых популярных фотографий пользователя.
    #
    #     :param user_id: Идентификатор пользователя ВКонтакте.
    #     :return: Список URL трех самых популярных фотографий.
    #     """
    #     # Реализуйте логику получения популярных фотографий здесь
    #     pass

    # def get_user_info(self, user_id):
    #     """
    #     Метод для получения информации о пользователе.
    #
    #     :param user_id: Идентификатор пользователя ВКонтакте.
    #     :return: Информация о пользователе (имя, фамилия, ссылка на профиль и т.д.).
    #     """
    #     # Реализуйте логику получения информации о пользователе здесь
    #     pass



    # def send_message(self, user_id, message, keyboard=None):
    #     try:
    #         params = {'user_id': user_id, 'message': message}
    #         if keyboard:
    #             params['keyboard'] = keyboard
    #         self.vk.method('messages.send', params)
    #     except vk_api.exceptions.ApiError as e:
    #         raise Exception(f"Error sending message: {e}")

