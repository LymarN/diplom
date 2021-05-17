import telebot
bot = telebot.TeleBot('1601183976:AAFO62JAtT2Sy_1hDU-Is5bEDMzGI8srqbE')
keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard1.row('Спеціальність', 'Категорія', 'Рейтинг', 'Про бот')
keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard2.row('121', '123', '141С', '141С', 'Повернутися')
keyboard3 = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard3.row('Доступність', 'Повернутися')
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard.row('1', '2', 'Повернутися')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю!❤️😉 \n'
    'Цей бот створений для об’єктивного оцінювання стилю викладання викладачів.'
    'Обери спеці альність, в якій викладає ваш викладач', reply_markup=keyboard1)
@bot.message_handler()
def send_text(message):
    if message.text.lower() == 'спеціальність':
        bot.send_message(message.chat.id, 'Обери потрібну спеціальність⏳', reply_markup=keyboard2)
    elif message.text.lower() == 'спеціальність 121':
        bot.send_message(message.chat.id, 'Обери потрібного викладача⏳', reply_markup=keyboard3)
    elif message.text.lower() == 'спеціальність 123':
        bot.send_message(message.chat.id, ' Обери потрібного викладача ⏳ \n', reply_markup=keyboard)
    elif message.text.lower() == 'спеціальність 141С':
        bot.send_message(message.chat.id, ' Обери потрібного викладача ⏳ \n', reply_markup=keyboard)
    elif message.text.lower() == 'спеціальність 141Е':
        bot.send_message(message.chat.id, ' Обери потрібного викладача ⏳ \n', reply_markup=keyboard)
    elif message.text.lower() == 'категорія':
        bot.send_message(message.chat.id, 'Обери потрібну категорію⏳', reply_markup=keyboard2)
    elif message.text.lower() == 'повернутися':
        bot.send_message(message.chat.id, 'Обери потрібну спеціальність', reply_markup=keyboard2)
    elif not message.text.isdigit():
        bot.send_message(message.chat.id, "Ви ввели не правильне повідомлення")
        return
bot.polling()
