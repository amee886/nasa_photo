import telegram
bot = telegram.Bot(token='7904978015:AAF5K8b508yayzalS4P6CI0ilavz77eSYAY')
chat_id="@SpaceXandSpace"
bot.send_message(text="Hi",chat_id=chat_id)
bot.send_photo(chat_id=chat_id,
               photo=open(r"E:\python\kurs\images\nasa_images\nasa_apod_0.jpg","rb")
               )
