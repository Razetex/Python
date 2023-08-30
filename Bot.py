import telebot
from config import keys, TOKEN
from extensions import APIException, ValueConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты, цену которой вы хотите узнать> \
    <В какую валюту перевести> \
    <Кол-во переводимой валюты> \nЧтобы увидеть список всех доступных валют введите: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: \n' + '\n'.join(keys.keys())
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException("Неправильные параметры. Воспользуйтесь /help для помощи.")

        base, quote, amount = values
        converted_amount = ValueConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя: {e}')
    except Exception as e:
        bot.reply_to(message, f'Произошла ошибка: {e}')
    else:
        text = f'Цена {amount} {base} в {quote} - {converted_amount:.2f}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)

