#astrasuperbot

import telebot

botTimeWeb = telebot.TeleBot('6858501529:AAFfSeF8cyJDeKGJTxPKL3v9GfMvBFSqW1M')

from telebot import types

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь узнать хороший ты человек или нет?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да, хочу', callback_data='yes')
  markup.add(button_yes)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Мы просканировали твое лицо...Узрей истину!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Узнать кто ты!", url="https://embassies.gov.il/moscow/NewsAndEvents/not_only_politics/PublishingImages/shutterstock_93846745-580x387.jpg"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()
