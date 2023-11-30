import time
from vk_api.longpoll import VkLongPoll, VkEventType
from bot.my_vk_api import VKApi  # Измененное имя файла

def handle_message(vk_api, event):
    user_id = event.user_id
    text = event.text
    print(f"Received message from user {user_id}: {text}")
    vk_api.send_message(user_id, f"Вы написали: {text}")

    if text.lower() == '/start':
        vk_api.send_message(user_id, 'Привет! Это бот. Выберите цифру от 1 до 3:')
        vk_api.send_message(user_id, '1. Начать поиск')
        vk_api.send_message(user_id, '2. Посмотреть избранных')
        vk_api.send_message(user_id, '3. Выйти')

    elif text.isdigit() and 1 <= int(text) <= 3:
        selected_number = int(text)
        vk_api.send_message(user_id, f'Вы выбрали цифру {selected_number}. Теперь я могу начать поиск.')

        if selected_number == 1:
            vk_api.send_message(user_id, 'Вы выбрали цифру 1. Начинаю поиск...')
            # Добавьте код для начала поиска и вывода информации о пользователях
        elif selected_number == 2:
            vk_api.send_message(user_id, 'Вы выбрали цифру 2. Показываю избранных...')
            # Добавьте код для вывода списка избранных пользователей
        elif selected_number == 3:
            vk_api.send_message(user_id, 'Вы выбрали цифру 3. Выход из программы.')
            # Добавьте код для выхода из программы

    else:
        vk_api.send_message(user_id, 'Я не понимаю. Пожалуйста, введите /start для начала.')

def main():
    group_token = open("group_token").read().strip()
    user_token = "USER_ACCESS_TOKEN"

    vk_group_session = VKApi(user_token, group_token)
    longpoll = VkLongPoll(vk_group_session.vk)

    print("Bot is running...")

    for event in longpoll.listen():
        print(f"Received event: {event}")
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_message(vk_group_session, event)

            # Добавьте обработку других команд
            # if event.text.lower() == '/start':
            #     vk_group_session.send_message(event.user_id, 'Привет! Это бот. Давай начнем!')

if __name__ == "__main__":
    main()

# def handle_message(vk_api, user_id, message):
#     print(f"Received message from user {user_id}: {message}")
#     if message.lower() == '/start':
#         vk_api.send_message(user_id, 'Привет! Я бот. Для начала работы напишите что-нибудь еще.')
#         print("Sent response to /start command")
#     else:
#         vk_api.send_message(user_id, f"Вы написали: {message}")
#         print("Sent response to other command")

            # Добавьте обработку других команд

    # vk_group_api = VKApi(user_token, group_token)
    # vk_user_api = VKApi(user_token)

    # # Основная логика работы бота
    # while True:
    #     # Получение новых событий/сообщений из группы
    #     # Реализуйте эту часть, используя VK Long Poll API или Callback API
    #
    #     # Обработка каждого нового события
    #     for event in new_events:
    #         if event['type'] == 'message_new':
    #             user_id = event['object']['message']['from_id']
    #             text = event['object']['message']['text']
    #
    #             # Определение команд и выполнение соответствующих действий
    #             if text.lower() == 'поиск':
    #                 criteria = {}  # Задайте критерии поиска, возможно, через диалог с пользователем
    #                 users = vk_group_api.search_users(criteria)
    #
    #                 for user in users:
    #                     user_info = vk_group_api.get_user_info(user['id'])
    #                     top_photos = vk_group_api.get_top_photos(user['id'])
    #
    #                     # Отправка информации о пользователе и фотографий
    #                     vk_group_api.send_message(user_id,
    #                                               f"{user_info['first_name']} {user_info['last_name']}\n{user_info['profile_link']}")
    #                     for photo_url in top_photos:
    #                         vk_group_api.send_message(user_id, attachment=photo_url)
    #
    #             elif text.lower() == 'избранные':
    #                 favorites = vk_group_api.get_favorites()
    #                 # Отправка списка избранных пользователей
    #                 vk_group_api.send_message(user_id, str(favorites))
    #
    #             # Другие команды обработки


