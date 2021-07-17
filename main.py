import re
import telebot
from os import environ

TOKEN = environ['TOKEN']
ADMIN_ID = environ['ADMIN_ID']

bot = telebot.TeleBot(TOKEN)
bot.send_message(ADMIN_ID, '\U0001f600')

dict = {
    "mmm": "а",
    "mmp": "б",
    "mmf": "в",
    "mpm": "г",
    "mpp": "д",
    "mpf": "е",
    "mfm": "ж",
    "mfp": "з",
    "mff": "и",
    "pmm": "к",
    "pmp": "л",
    "pmf": "м",
    "ppm": "н",
    "ppp": "о",
    "ppf": "п",
    "pfm": "р",
    "pfp": "с",
    "pff": "т",
    "fmm": "у",
    "fmp": "ф",
    "fmf": "х",
    "fpm": "ч",
    "fpp": "ш",
    "fpf": "ь",
    "ffm": "э",
    "ffp": "ю",
    "fff": "я",
    "MMM": "А",
    "MMP": "Б",
    "MMF": "В",
    "MPM": "Г",
    "MPP": "Д",
    "MPF": "Е",
    "MFM": "Ж",
    "MFP": "З",
    "MFF": "И",
    "PMM": "К",
    "PMP": "Л",
    "PMF": "М",
    "PPM": "Н",
    "PPP": "О",
    "PPF": "П",
    "PFM": "Р",
    "PFP": "С",
    "PFF": "Т",
    "FMM": "У",
    "FMP": "Ф",
    "FMF": "Х",
    "FPM": "Ч",
    "FPP": "Ш",
    "FPF": "Ь",
    "FFM": "Э",
    "FFP": "Ю",
    "FFF": "Я",
}


def multiple_replace(dict, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def translate(msg):
    prefix, text = msg.split(':', 1)
    translated_text = multiple_replace(dict, text)
    return prefix + ': ' + translated_text


@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_sticker = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, welcome_sticker)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        msg = message.text
        result = translate(msg)
        bot.send_message(message.chat.id, result)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка')


bot.polling(none_stop=True, interval=0.2)
