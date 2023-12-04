import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random

def write_msg(vk, user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=get_random_id())

def get_basic_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Один', color=VkKeyboardColor.PRIMARY, payload={'additional_info': 'some info'})
    keyboard.add_button('Два', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('Три', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Старт', color=VkKeyboardColor.POSITIVE)
    return keyboard

def get_random_id():
    return random.randint(1, 1000000)

def send_help_message(vk, user_id):
    rules_message = 'Добро пожаловать! Это бот. Вот некоторые команды, которые вы можете использовать:\n' \
                    '1. Начать поиск\n' \
                    '2. Посмотреть избранных\n' \
                    '3. Добавить в блэклист\n' \
                    '4. Выйти'

    basic_keyboard = get_basic_keyboard()
    random_id = get_random_id()

    params = {
        'user_id': user_id,
        'message': rules_message,
        'keyboard': basic_keyboard.get_keyboard(),
        'random_id': random_id
    }

    vk.messages.send(**params)

def handle_message(vk, event):
    user_id = event.user_id
    text = event.text.strip()
    print(f"Received message from user {user_id}: {text}")

    try:
        vk.messages.send(user_id=user_id, message=f"Вы написали: {text}")
        write_msg(vk, user_id, f'Бот ответил на ваше сообщение: {text}')
    except Exception as e:
        print("Message sent successfully.")
        print(f"Error sending message: {e}")

    send_help_message(vk, user_id)  # Отправляем правила после любого входящего сообщения

def main():
    group_token_path = "group_token"
    group_id = 223624883

    with open(group_token_path, 'r') as group_token_file:
        group_token = group_token_file.read().strip()

    vk_group_session = vk_api.VkApi(token=group_token)
    vk = vk_group_session.get_api()
    longpoll = VkBotLongPoll(vk_group_session, group_id)

    print("Bot is running...")

    for event in longpoll.listen():
        print(f"Received event: {event}")
        if event.type == VkBotEventType.MESSAGE_NEW:
            handle_message(vk, event)

if __name__ == "__main__":
    main()