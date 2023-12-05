import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random

def write_msg(vk, user_id, message):
    vk.messages.send(user_id=user_id, message=message, random_id=get_random_id())

def get_basic_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('1', color=VkKeyboardColor.PRIMARY, payload={'additional_info': 'some info'})
    keyboard.add_button('2', color=VkKeyboardColor.SECONDARY)
    keyboard.add_button('3', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('4', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('ХауТу', color=VkKeyboardColor.POSITIVE)
    return keyboard

def get_random_id():
    return random.randint(1, 1000000)

def send_help_message(vk, user_id):
    rules_message = 'Добро пожаловать! Это бот. Вот некоторые команды, которые вы можете использовать:\n' \
                    '1. Ищем пару\n' \
                    '2. Добавим в избранное\n' \
                    '3. Покажем избранное\n' \
                    '4. Добавим в БлэкЛист\n' \
                    '5. ХАУТУ'

    basic_keyboard = get_basic_keyboard()
    random_id = get_random_id()

    params = {
        'user_id': user_id,
        'message': rules_message,
        'keyboard': basic_keyboard.get_keyboard(),
        'random_id': random_id
    }

    try:
        vk.messages.send(**params)
        print("Help message sent successfully.")
    except Exception as e:
        print("Error sending help message: {e}")

def send_find_pair_message(vk, user_id):
    print("find_pair")
    response_message = 'Начинаем поиск пары для вас!'
    write_msg(vk, user_id, response_message)

def send_add_to_favorites(vk, user_id):
    print("Add_to_favorites")
    response_message = 'Добавляем в избранное!'
    write_msg(vk, user_id, response_message)

def send_show_favorites(vk, user_id):
    print("Show_favorites")
    response_message = 'Показываем избранное!'
    write_msg(vk, user_id, response_message)

def send_add_to_blacklist(vk, user_id):
    print ("Add to blackList")
    response_message = 'Добавляем в черный список!'
    write_msg(vk, user_id, response_message)

def handle_message(vk, event):
    user_id = event.message['from_id']
    text = event.message['text'].strip()
    print(f"Received message from user {user_id}: {text}")

    try:
        vk.messages.send(user_id=user_id, message=f"Вы написали: {text}")
        write_msg(vk, user_id, f'Бот ответил на ваше сообщение: {text}')
    except Exception as e:
        print("Message sent successfully.")
        print(f"Error sending message: {e}")

    if text == '1':
        send_find_pair_message(vk, user_id)
    elif text == '2':
        send_add_to_favorites(vk, user_id)
    elif text == '3':
        send_show_favorites(vk, user_id)
    elif text == '4':
        send_add_to_blacklist(vk, user_id)
    elif text=='ХауТу':
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