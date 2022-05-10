import telebot 
 
bot = telebot.TeleBot("5329504751:AAEKcRi2sCsdLjbZKMwoFLGJIOEPNFS2i9Y") 
 
 
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Добрый день, географ! Третий вопрос! https://theidealist.ru/wp-content/uploads/2021/06/cernobilj-1200x800.jpeg Угадай страну и город!")
    # задаётся третий вопрос

@bot.message_handler(func=lambda n: True) 
def echo_all(message):
    if message.text == 'Россия, Чернобыль':
        bot.reply_to(message, 'Поздравляю, вы правильно ответили на третий вопрос! Спасибо за участие в суперигре! https://vk.com/away.php?utf=1&to=https%3A%2F%2Favatars.mds.yandex.net%2Fget-zen_doc%2F1873182%2Fpub_5dab22754e057700b17c737e_5dab33d5e6e8ef00b18f20a0%2Fscale_1200')
    else:
        bot.reply_to(message, 'К сожалению, вы не ответили на 3 вопрос. Спасибо за участие! ')
        # ответ на третий вопрос и финал

 
bot.polling()