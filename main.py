import topics
import difflib


token = '5235271982:AAErJJ4zD6K7sWkdLOYrX6u3cdUWrNX6gT4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # Команда приветствия
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Алгебра")
    btn2 = types.KeyboardButton("Геометрия")
    btn3 = types.KeyboardButton("Информатика")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Привет! Это бот со школьными темами.\nВыберите интересующий предмет', reply_markup=markup)
