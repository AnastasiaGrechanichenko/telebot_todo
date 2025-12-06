import telebot
from telebot import types
from TaskManager import TaskManager


token= ('8593774051:AAHOi9kCXGdlXmTX0DrbByaMkHTHn_jb-fg')
bot=telebot.TeleBot(token) #bot — это экземпляр класса TeleBot из библиотеки pyTelegramBotAPI.

taskManager = TaskManager()

cache = {}

def check_create_button(message):
    return message.text =="Создать задачу"

def check_show_button(message):
    return message.text == "Показать задачи"


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_create = types.KeyboardButton("Создать задачу")
    button_show = types.KeyboardButton("Показать задачи")
    markup.add(button_create,button_show)
    return markup

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️. Выбери действие: ",reply_markup=main_menu()
                     )

@bot.message_handler(func=check_create_button)
def handle_create_button(message):
    create_task(message)

@bot.message_handler(func=check_show_button)
def handle_show_button(message):
    start_message_show(message)

@bot.message_handler(commands=['show'])
def start_message_show(message):
    tasks = taskManager.get_str_tasks()
    bot.send_message(message.chat.id, f"{tasks}")

@bot.message_handler(commands=['create']) #Если пользователь отправляет команду /create, то выполни функцию create_task
def create_task(message):
    chat_id = message.chat.id
    cache [str(chat_id)] = {} #chat_id для запоминания конкретного пользователя
    msg = bot.reply_to(message,"Введите название задачи ✌️ ")
    bot.register_next_step_handler(msg,process_name)

def process_name(message):
    try:
        chat_id = message.chat.id
        cache[str(chat_id)]['name'] = message.text
        msg = bot.reply_to(message,"Введите описание задачи")
        bot.register_next_step_handler(msg,process_desc)
    except Exception as ex:
        bot.reply_to(message,"ошибочка")


def process_desc(message):
    try:
        chat_id = message.chat.id
        cache[str(chat_id)]['description'] = message.text
        taskManager.create_task(cache[str(chat_id)]['name'],cache[str(chat_id)]['description'])
        bot.reply_to(message,"Задача успешно добавлена!")
    except Exception as ex:
        bot.reply_to(message,"что-то не так")


bot.infinity_polling() # Это вечный цикл, который постоянно опрашивает серверы Telegram на наличие новых сообщений.