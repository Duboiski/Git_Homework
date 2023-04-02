import telebot, requests, random
from telebot import types
from bs4 import BeautifulSoup as bs

token = '6110029890:AAEQb6AJ89BCrtN1O_EikrzqfnnwWggEX50'
bot = telebot.TeleBot(token)
URL = 'https://www.anekdot.ru/last/good/'

def parser(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anecdots = soup.find_all('div', class_ = 'text')
    return [i.text for i in anecdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
def my_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    hi_btn = types.InlineKeyboardButton(text='Привет', callback_data='1')
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='2')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='3')
    anecdote_btn = types.InlineKeyboardButton(text='Хочу анегдот', callback_data='4')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='5')
    bye_btn = types.InlineKeyboardButton(text='Прощание с ботом', callback_data='6')
    keyboard.add(hi_btn, drink_btn, eat_btn, anecdote_btn, sleep_btn, bye_btn)
    return keyboard
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Привет! Выбирите что бы вы хотели: ', reply_markup=my_keyboard())
    img = 'https://www.imagetext.ru/pics_max/images_1560.jpg'
    bot.send_photo(message.chat.id, photo=img, caption='Приветственная картинка',
                   reply_markup=my_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '1':
            img = 'https://www.imagetext.ru/pics_max/images_1560.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Приветственная картинка', reply_markup=my_keyboard())

        if call.data == '2':
            img = 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Water_drop_impact_on_a_water-surface_-_%282%29.jpg'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка воды', reply_markup=my_keyboard())

        if call.data == '3':
            img = open('1559545617_2.jpg',
                       'rb')
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка еды', reply_markup=my_keyboard())

        if call.data == '4':
            bot.send_message(chat_id=call.message.chat.id, text=list_of_jokes[0], reply_markup=my_keyboard())
            del list_of_jokes[0]

        if call.data == '5':
            img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3HA-EX-ONk03oXbtKHZ-ppGX5zXYA-pG6-Q&usqp=CAU'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Хочу спать', reply_markup=my_keyboard())

        if call.data == '6':
            img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWgIAEwog1R4McpAnA5klL2iIikboPulvCLzo0Xs8igx4BmGeH4SK3DPROCgWJ1t_V7Jo&usqp=CAU'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Пока', reply_markup=my_keyboard())
            img.close()

bot.polling(none_stop=True)