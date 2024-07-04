from requests import get

from environs import Env

env = Env()
env.read_env()


def sent_message(order):
    token = env.str('BOT_TOKEN')

    chat_id = env.str('CHAT_ID')

    text = f' - raqamli to\'lov amalga oshirildi ************ ' \
           f' ta odamga to\'lov qilindi ************ ' \
           f'Summa miqdori:  so\'m ************ ' \
           f'Xaridor: ************ ' \
           f'Telefon raqami:  ************ ' \

    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    try:
        _ = get(url)
    except:
        print('Telegramga ma\'lumot jo\'natishda xatolik')