import asyncio
import telebot

bot = telebot.TeleBot('5834237694:AAE0TJdYohtj69L6jsXmD2MB0vFcsWB8tpA')


def send():
    results = open('result.txt', 'r')
    msg = results.read()
    bot.send_message(412997019, msg)

send()


bot.polling(none_stop=True, interval=0)