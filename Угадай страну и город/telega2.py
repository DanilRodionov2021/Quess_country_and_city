import telebot 
 
bot = telebot.TeleBot("5381495044:AAFkTlcFQdTDKLsMb0ITJahT8jktsR2h7GU") 
 
 
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Приветствую вас, участник игры! Первый вопрос! https://kartinkin.net/uploads/posts/2021-03/1616086788_51-p-berlin-krasivie-foto-58.jpg Угадай страну и город!")
 
@bot.message_handler(func=lambda n: True) 
def echo_all(message):
    if message.text == 'Германия, Берлин':
        bot.reply_to(message, 'Поздравляю, вы правильно ответили на первытй вопрос! Перейдите по ссылке на второй вопрос: http://t.me/Voronesh_Donskoe_bot.')
    else:
        bot.reply_to(message, 'К сожалению, вы не ответили на первый вопрос. Будем надеяться, что ответите на остальные вопросы! Перейдите по ссылке на второй вопрос: http://t.me/Voronesh_Donskoe_bot. ')
     
 
bot.polling()