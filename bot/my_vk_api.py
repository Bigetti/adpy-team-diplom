import requests
import json


class VKapi:

    def __init__(self, vk_user_token, group_token):
        self.user_token = vk_user_token
        self.group_token = group_token
        self.api_version = "5.131"
        self.base_url = "https://api.vk.com/method/"

    def send_message(self, user_id, message, attachment=None):
        """
        Метод для отправки сообщения пользователю.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :param message: Текст сообщения.
        :param attachment: Вложение (например, фотография).
        :return: Результат отправки (успех или ошибка).
        """
        params = {
            'user_id': user_id,
            'message': message,
            'attachment': attachment,
            'access_token': self.group_token,
            'v': self.api_version
        }
        response = requests.post(self.base_url + 'messages.send', params=params)
        return response.json()

    def search_users(self, criteria):
        """
        Метод для поиска пользователей ВКонтакте.

        :param criteria: Критерии поиска (возраст, пол, город и т.д.).
        :return: Список пользователей, соответствующих критериям.
        """
        # Реализуйте логику поиска пользователей здесь
        pass

    def get_top_photos(self, user_id):
        """
        Метод для получения трех самых популярных фотографий пользователя.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :return: Список URL трех самых популярных фотографий.
        """
        # Реализуйте логику получения популярных фотографий здесь
        pass

    def get_user_info(self, user_id):
        """
        Метод для получения информации о пользователе.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :return: Информация о пользователе (имя, фамилия, ссылка на профиль и т.д.).
        """
        # Реализуйте логику получения информации о пользователе здесь
        pass

    def add_to_favorites(self, user_id):
        """
        Метод для добавления пользователя в список избранных.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :return: Результат операции (успех или ошибка).
        """
        # Реализуйте логику добавления пользователя в избранные здесь
        pass

    def add_to_black_list(self, user_id):
        """
        Метод для добавления пользователя в черный список.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :return: Результат операции (успех или ошибка).
        """
        # Реализуйте логику добавления пользователя в черный список здесь
        pass

    def get_favorites(self):
        """
        Метод для получения списка избранных пользователей.

        :return: Список избранных пользователей.
        """
        # Реализуйте логику получения списка избранных пользователей здесь
        pass