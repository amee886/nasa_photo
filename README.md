# Nasa Photo Gallery

Nasa Photo Gallery - это веб-приложение,которое позволяет пользователям просматривать фотографии и изображения, предоставленные Nasa. Используя API NASA, приложение загружает и отображает различные изображения, включая астрономические снимки, фотографии миссий и другие визуальные материалы.

## 1.Установка

```bash
git clone https://github.com/amee886/nasa_photo.git cd nasa_photo
```

Убедитесь, что у вас установлен Python 3.6 или выше. Затем установите необходимые зависимости:
   
```bash
   python -m pip install -r requirements.txt
```

## 2.Описание функций
-**fetch_spacex_last_launch**(launch_id): скачивает изображения запуска ракеты из другого репозитория используя id запуска.

<img width="418" height="126" alt="image" src="https://github.com/user-attachments/assets/c6d1db04-e56d-457c-b1e3-b28ab5f0a2c7" />

-**APOD**(nasa_api_key): скачивает лучшие снимки дня с сайта Nasa в отдельную директорию.

<img width="93" height="115" alt="image" src="https://github.com/user-attachments/assets/8357cfd5-e4c5-4ddc-805a-196c615d5703" />

-**EPIC**(limit,nasa_api_key): скачивает снимки нашей планеты с сайта Nasa в отдельную директорию.

<img width="118" height="127" alt="image" src="https://github.com/user-attachments/assets/b2495d8f-68bd-4176-888c-9ca756ca3065" />

-**tg_bot**(chat_id,time_sleep,bot):создает телеграм бота который сам отправляет фотографии в телеграм-канал, а после того как все оптравит перемешивает их и дальше продолжает.

<img width="848" height="606" alt="image" src="https://github.com/user-attachments/assets/945c3a6b-f062-41eb-8dba-d4efeddc36fe" />


## 3. Получите API Nasa
Вам нужно будет зарегестрироваться на сайте NASA и получить API_key.Для этого выполните следующие шаги:
1. Перейдите на [страницу регистрации API NASA](https://api.nasa.gov).
2. Зарегистрируйтесь и получите свой уникальный ключ.

## 4. Настройте переменные окружения:

Создайте файл .env в корневом каталоге проекта и добавьте туда ваш токен:

   
NASA_API_KEY=ваш ключ NASA
TG_API_TOKEN=токен вашего бота

## 5. Канал

Создайте телеграм канал где бот будет администратором

## 6. Запуск

Запустите скрипт fetch_spacex_last_launch и укажите id запуска ракеты

```bash
python fetch_spacex_last_launch.py id запуска
```

Запустите скрипт tg_bot и укажите время паузы между фотографиями

```bash
python tg_bot.py ваше время
```
## Цели проекта

Код написан в образовательных целях для онлайн-курса для веб-разработчиков [dvmn.org](https://dvmn.org/modules/).

   
