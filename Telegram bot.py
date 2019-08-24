import telebot
import config
import datetime
from datetime import * #to allow the bot to use time and dates

bot = telebot.TeleBot(config.token) #connects bot token to script
task = ''
datatext = ''


@bot.message_handler(commands=['start']) #starts up the bot
def start(message):
    ab = bot.send_message(message.chat.id, 'What do you need help remembering? Enter a short description:')
    bot.register_next_step_handler(ab, answer)

@bot.message_handler(content_types=['text'])#saves task
def answer(message):
    global task
    task = message.text
    msg = bot.send_message(message.chat.id, 'What day and time do you need to be reminded? (dd/mm/yyyy hh:mm)')
    bot.register_next_step_handler(msg, answer2)
        
@bot.message_handler(content_types=['text'])#saves time for task
def answer2(message):
    global task
    global datatext
    global timetoday

    datatext = message.text
    
    bot.send_message(message.chat.id, 'Ok, I will remind you to '+ task+' at '+datatext)

    while True:
        timetoday = datetime.now() #reads the time and date on user's system
        dt_string = timetoday.strftime("%d/%m/%Y %H:%M")
        if datatext == dt_string:
            bot.send_message(message.chat.id, 'Reminder to '+task)
            break


if __name__ == '__main__':
    bot.polling(none_stop=True)
