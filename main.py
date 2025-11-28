import telebot
from TaskManager import TaskManager

token='8340772869:AAFjDgh_U9NuODQxh0OdmGw8r1a65haOdYY'
bot=telebot.TeleBot(token) #bot — это экземпляр класса TeleBot из библиотеки pyTelegramBotAPI.

taskManager = TaskManager()

cache = {} '''cache = {
    123456789: "ожидание названия задачи", 
    987654321: "ожидание описания задачи"
}
где 123456789 и 987654321 — это user_id
словарь, ключ юзер айди
'''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")


# начало создания задачи
@bot.message_handler(commands=['create'])
'''
"Если пользователь отправляет команду /create, то выполни функцию create_task."
'''
def create_task(message):
    chat_id = message.chat.id
    cache [str(chat_id)] = {} #chat_id для запоминания конкретного пользователя
    msg = bot.reply_to(message,"Введите название задачи ✌️ ")
    bot.register_next_step_handler(msg,process_name)
def get_task_name(message):
    task_name = message.text

@bot.message_handler(commands=['show'])
def start_message(message):
    tasks = taskManager.get_tasks()
    bot.send_message(message.chat.id,f"{tasks}")

bot.infinity_polling() # Это вечный цикл, который постоянно опрашивает серверы Telegram на наличие новых сообщений.