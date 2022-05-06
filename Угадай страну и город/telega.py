import telebot;

bot = telebot.TeleBot('5160177317:AAE10XVzZpo1d-JhkBtTTcrQlKMfQUHuRi0');

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Здравствуй, мой юный географ! Вы готовы к суперигре УГАДАЙ СТРАНУ И ГОРОД?")
 
@bot.message_handler(func=lambda n: True) 
def echo_all(message):
    if message.text == 'Да':
        bot.reply_to(message, 'Ну что ж, тогда начинаем игру! Перейдите по ссылке на первый вопрос: http://t.me/Dan4ix_bot.')
    else:
        bot.reply_to(message, 'Ну что ж, тогда всего хорошего!')
     
 
bot.polling()