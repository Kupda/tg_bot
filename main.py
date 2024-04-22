import telebot
from telebot import types
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


dict1 = {
    "Алгебра": topics.algebra,
    "Геометрия": topics.geometry,
    "Информатика": topics.informatics
}


@bot.message_handler(content_types=['text'])
def get_topics(message):
    global topic
    global list1
    topic = message.text
    try:
        list1 = dict1.get(topic).keys()
        bot.send_message(message.chat.id, 'Введите интересующую для вас тему')
        bot.register_next_step_handler(message, get_text_messages1)
    except:
        bot.send_message(message.chat.id,
                         'Вы допустили ошибку в написание предмета\nВыбирайте предмет в клавиатуре телеграмма')
        bot.register_next_step_handler(message, get_topics)


@bot.message_handler(content_types=['text'])
def get_text_messages1(message):
    list2 = []
    markup = types.InlineKeyboardMarkup()
    for i in list1:
        if similarity(message.text, i) >= 0.45:  # Процент схожести
            list2.append(i)
    if list2:
        for i in list2:
            markup.add(types.InlineKeyboardButton(i, url=dict1.get(topic)[i]))
        bot.send_message(message.chat.id, 'Я нашел несколько тем, а именно...', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'К сожелению я ничего не нашел')
    bot.send_message(message.chat.id, 'Спасибо за использования бота! Если вам нужна еще тема, то введите название предмета')


def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


bot.polling(none_stop=True)