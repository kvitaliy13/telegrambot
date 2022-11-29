import telebot
from config import allval, TOKEN
from excep import ConvertionException, Converter
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("🔎 Условия пользования")
    btn2 = types.KeyboardButton("💸 Доступные валюты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f'Приветствую, {message.chat.first_name}!\nЭтот телеграмм бот поможет Вам конвертировать валюты.', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🔎 Условия пользования"):
        bot.send_message(message.chat.id, text=f"{message.chat.first_name}, для работы с ботом Вам необходимо ввести:\n <имя валюты>/ <в какую валюту перевести>/ <колличество валюты>\nПример: доллар рубль 100")
    elif (message.text == "💸 Доступные валюты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        text = 'Доступные валюты: '
        for i in allval.keys():
            text = '\n'.join((text, i))
        bot.send_message(message.chat.id, text)

    elif(message.text != '🔎 Условия пользования', '💸 Доступные валюты'):
        values = message.text.split(' ')
        try:

            if len(values) != 3:
                raise ConvertionException('Необходимо ввести 3 параметра')
            val1, val2, cash = values

            cash = Converter.convert(*values)
        except ConvertionException as e:
            bot.reply_to(message, f'Ошибка пользователя. \n{e}')
        except Exception as e:
            bot.reply_to(message, f'Не удалось обработать команду\n {e}')
        else:
            bot.reply_to(message, cash)

bot.polling(non_stop=True)

