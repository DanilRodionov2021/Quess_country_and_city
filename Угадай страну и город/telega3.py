import telebot 
 
bot = telebot.TeleBot("5275373837:AAESq6Nb5iCkLap0_3zVFoVWGY8_-jVToBY") 
 
 
@bot.message_handler(commands=["start", "help"])
def send_welcome(message): 
 bot.reply_to(message, "Здравствуй, участник игры! Второй вопрос! https://s1.1zoom.ru/b5050/453/Warsaw_Poland_Houses_Evening_512709_3840x2400.jpg Угадай страну и город!")
 
@bot.message_handler(func=lambda n: True) 
def echo_all(message):
 if message.text == 'Польша, Варшава':
     bot.reply_to(message, 'Поздравляю, вы правильно ответили на второй вопрос! Перейдите по ссылке на третий вопрос: http://t.me/Kiev_Minsk_bot')
 else:
     bot.reply_to(message, 'К сожалению, вы не ответили на второй вопрос. Будем надеяться, что ответите на последний вопрос! Перейдите по ссылке на последний вопрос: http://t.me/Kiev_Minsk_bot ') 
     
 
bot.polling()
