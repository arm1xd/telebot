import telebot
bot = telebot.TeleBot("5257223347:AAFsUGcsKnhUF6B9VxZnnjHEuwBSe_QuCz4")
@bot.message_handler(commands=['start','boba'])
def send_welcome(message):
 bot.reply_to(message, "Я твой персональный бот, давай знакомиться!")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет' для приветствия,'Как дела?' для вопроса о состояниия,'Пока' для прощания")
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Спасибо,все отлично")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Пока, рад был пообщаться")
    elif message.text == "Пайтон":
        bot.send_message(message.from_user.id, "НАВЕКИ, НАВЕКИ, ВОВЕКИ ВЕКОВ")
    elif message.text == "Денис":
        bot.send_message(message.from_user.id, "Денис лох й предал пайтон")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    
  
bot.infinity_polling()