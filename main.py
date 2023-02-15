import telebot
from config import keys, token
from extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def welcome(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты цену которой хотите узнать> \
<имя валюты в которой надо узнать цену первой валюты> \
<количество первой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
<<<<<<< HEAD
            raise ConvertionException('Введено слишком много параметров.')
=======
            raise ConvertionException('Введено неверное число параметров.')
>>>>>>> 3150a49 (Initial commit)

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
