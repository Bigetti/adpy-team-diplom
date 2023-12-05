import requests
import json
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import private_token


class BotApiVK:

    def __init__(self, vk_user_token, group_token):
        self.user_token = vk_user_token
        self.group_token = group_token
        self.api_version = 5.199
        # self.base_url = "https://api.vk.com/method/"
        self.vk = VkApi(token=self.group_token)
        self.vk.auth(token_only=True)
        self.longpoll = VkLongPoll(self.vk)

    def send_message(self, user_id, message, attachment, keyboard=None):
        """
        Метод для отправки сообщения пользователю.

        :param user_id: Идентификатор пользователя ВКонтакте.
        :param message: Текст сообщения.
        :param attachment: Вложение (например, фотография).
        :return: Результат отправки (успех или ошибка).
        """
        try:
            params = {'user_id': user_id, 'message': message}
            if keyboard:
                params['keyboard'] = keyboard
            self.vk.method('messages.send', params)
        except vk_api.exceptions.ApiError as e:
            raise Exception(f"Error sending message: {e}")

        self.vk.method("messages.send",
                       values={'random_id': random.randrange(10 ** 7),
                               'access_token': self.group_token,
                               'v': self.api_version,
                               'user_id': user_id,
                               'message': message,
                               'attachment': attachment,
                               })

        # self.vk.method("messages.send",
        #                values={'user_id': user_id,
        #                        'message': message,
        #                        'attachment': attachment,
        #                        'access_token': self.group_token,
        #                        'v': self.api_version})

        # params = {
        #     'user_id': user_id,
        #     'message': message,
        #     'attachment': attachment,
        #     'access_token': self.group_token,
        #     'v': self.api_version
        # }
        # response = requests.post(self.base_url + 'messages.send', params=params)
        # return response.json()


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


if __name__ == "__main__":
    bot_api = BotApiVK(private_token.USER_TOKEN, private_token.GROUP_TOKEN)
    for event in bot_api.longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                print(event, event.to_me)
                if request == "привет":
                    bot_api.send_message(event.user_id, f"Хай, {event.user_id}")
                elif request == "пока":
                    bot_api.send_message(event.user_id, "Пока((")
                else:
                    bot_api.send_message(event.user_id, "Не поняла вашего ответа...")
