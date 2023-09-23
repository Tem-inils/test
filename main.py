import telebot
import buttons

bot = telebot.TeleBot('6567697373:AAFYnPXktIQRVOWppXOzGfGbMY_65TI57FM')

@bot.message_handler(commands=['start'])
def message_start(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, f'{message.from_user.username} Добро пожаловать в бота Английского языка', reply_markup=buttons.type1())

@bot.message_handler(content_types=['text'])
def text_start(message):
    chat = str(message.text)
    if chat.lower() == 'таблицы':
        # Убираем текущую клавиатуру (ReplyKeyboardRemove)
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(user_id, 'Выберите интересующие вас правила', reply_markup=markup)
        # Отправляем новое сообщение с инлайн-кнопками и удаляем старое сообщение
        bot.send_message(user_id, 'Выберите интересующие вас правила', reply_markup=buttons.type2())
        bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
    else:
        bot.send_message(user_id, 'Используй кнопки для переходов')
        bot.register_next_step_handler(message, text_start)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "time_english":
        with open('englishphoto.jpg', 'rb') as file:
            bot.send_photo(call.message.chat.id, file, caption='Времена в Английском')
    # Добавьте обработку других инлайн-кнопок, если необходимо

bot.polling(none_stop=True)