import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN") 

user_state = {}

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.reply_to(message, "Hello! What do you want to do?") 
    show_main_menu(message.chat.id) 

def show_main_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    keyboard.add("Материалы для 3-d печати", "Сравнить материалы") 
    keyboard.add("Найти подходящий материал") 
    bot.send_message(chat_id, "Выбери действие:", reply_markup=keyboard) 

def materials_for_3_d_printing(chat_id):
    #кнопки с названием материалов
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    keyboard.add("PLA", "ABS") 
    keyboard.add("PETG", "Нейлон") 
    keyboard.add("FLEX", "Поликарбонат") 
    keyboard.add("К выбору действий") 
    bot.send_message(chat_id, "Выбери материал, о котором хочешь узнать.", reply_markup=keyboard) 

def comparison(chat_id):
    #кнопки с названием материалов
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("PLA, ABS", "PLA, PETG", "PLA, Нейлон")
    keyboard.add("PLA, FLEX", "PLA, Поликарбонат", "ABS, PETG")
    keyboard.add("ABS, Нейлон", "ABS, FLEX", "ABS, Поликарбонат")
    keyboard.add("PETG, Нейлон", "PETG, FLEX", "PETG, Поликарбонат") 
    keyboard.add("Нейлон, FLEX", "Нейлон, Поликарбонат", "FLEX, Поликарбонат")
    keyboard.add("К выбору действий")
    bot.send_message(chat_id, "Выбери материал для сравнения.", reply_markup=keyboard) 

def find_material(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    keyboard.add("Да", "Нет") 
    keyboard.add("Не знаю", "Возможно") 
    keyboard.add("Сомневаюсь") 
    keyboard.add("К выбору действий")
    bot.send_message(chat_id, "вопрос", reply_markup=keyboard) 

def back(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Назад")

@bot.message_handler(func=lambda message: True) 
def handle_messages(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Материалы для 3-d печати":
        materials_for_3_d_printing(chat_id)

    elif text == "Сравнить материалы":
        comparison(chat_id)

    elif text == "Найти подходящий материал":
        find_material(chat_id)

    elif text == "PLA":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о PLA пластике: ")

    elif text == "ABS":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о ABS пластике: ")

    elif text == "PETG":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о PETG пластике: ")

    elif text == "Нейлон":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о Нейлон пластике: ")

    elif text == "FLEX":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о FLEX пластике: ")

    elif text == "Поликарбонат":
        back(chat_id)
        bot.send_message(chat_id, "Вот информация о Поликарбонат пластике: ")

    elif text == "Назад":
        materials_for_3_d_printing(chat_id)

    elif text == "К выбору действий":
        show_main_menu(chat_id)


bot.polling()
