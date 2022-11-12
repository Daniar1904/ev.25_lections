import telebot
from MyToken import token
from telebot import types

# InlineKeyboardMerkup
# ReplyKeyboardMerkup

bot = telebot.TeleBot(token)

inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Доход', callback_data='income')
btn2 = types.InlineKeyboardButton('Расход', callback_data='costs')
inline_keyboard.add(btn1, btn2)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! Сделайте выбор!', reply_markup=inline_keyboard)

@bot.callback_query_handler(func = lambda c: True)
def inline(c): #message.text
    if c.data == 'income':
        income_keyboard = types.ReplyKeyboardMarkup()
        k1 = 



    










# @bot.message_handler(commands=['start', 'hello'])
# def start_message(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, "Hello!!! I'm Python_Test Bot!") 

# @bot.message_handler(content_types=['sticker', 'text'])
# def send_sticker(message):
#     chat_id = message.chat.id
#     if message.text.lower() == 'hello':
#         bot.send_message(chat_id, 'Hello, my Dear!')
#     bot.send_sticker(chat_id, "CAACAgIAAxkBAAEGZDtjb2IhLatcVYbLClZXXTgZBvlZzgACGwAD2dDlMN78mPxmybjaKwQ")


bot.polling()