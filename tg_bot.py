import telegram
import time
import os
import random
from decouple import config
import argparse


def post_images_to_channel(chat_id, time_sleep, bot):
    photo_dir = os.path.join(os.path.dirname(__file__), 'nasa_images')
    photos = [os.path.join(photo_dir, f)
              for f in os.listdir(photo_dir)
              if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif'))]
    photos.sort()
    while True:
        for photo_path in photos:
            try:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
            except Exception as e:
                print(f"Ошибка при отправке {photo_path}: {e}")
            time.sleep(time_sleep)
        random.shuffle(photos)


def main():
    parser = argparse.ArgumentParser(description='Бот сам отправляет фотографии из директории в телеграм канал с определенным промежутком')
    parser.add_argument('time', type=int, help='время между отправлением фотографий в секундах')
    args = parser.parse_args()
    time_sleep = args.time
    chat_id = config("CHAT_ID")
    tg_api_token = config("TG_API_TOKEN")
    bot = telegram.Bot(token=tg_api_token)
    try:
        bot.send_message(chat_id=chat_id, text="Бот запущен и готов к отправке фотографий!")
    except telegram.error.TelegramError as e:
        print(f"Не удалось отправить приветственное сообщение: {e}")
    sends_photos(chat_id, time_sleep, bot)


if __name__ == "__main__":
    main()


