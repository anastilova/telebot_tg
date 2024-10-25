import telebot
from telebot import types

bot = telebot.TeleBot('7733456899:AAHRl6BIVEpil8R_ck_Ohe17Eghmzz-XS5Y')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('✅ Получить ссылку на канал! ✅')
    btn2 = types.KeyboardButton('Анекдот дня')
    markup.row(btn1)
    markup.row(btn2)
    full_name = f"{message.from_user.first_name}"
    if message.from_user.last_name:
        full_name += f"{message.from_user.last_name}"
    bot.send_message(message.chat.id, f'Привет, {full_name}!\n' + 'Я твой помощник <b>DevOps_bot</b>', parse_mode='html',
                     reply_markup=markup)  # чтоб кнопки отображались
    # bot.register_next_step_handler(message, add_email) бот ожидает ввод email сразу после старта


@bot.message_handler(func=lambda message: True) # Обработчик для всех текстовых сообщений
def handle_message(message):
    if message.text == '✅ Получить ссылку на канал! ✅':
        show_cancel_button(message)
        add_email(message)
    elif message.text == 'Анекдот дня':
        show_cancel_button(message)
        smile(message)

def show_cancel_button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton('Отмена')
    markup.add(btn3)
    #bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

def smile(message):
    if message.text == 'Анекдот дня':
        btn3 = types.KeyboardButton('Отмена')
        bot.send_message(message.chat.id, "Настало время переходить с летних колёс на зимние!\nМашины у меня нет, я про антидепрессанты.")

def add_email(message):
    if message.text == '✅ Получить ссылку на канал! ✅' :
        bot.send_message(message.chat.id, "✏️ Для получения ссылки на канал введите, пожалуйста, адрес своей корпоративной почты .ru!")
        bot.register_next_step_handler(message, save_email)
def save_email(message):
    email = message.text
    with open('emails.txt', 'a') as file:
        file.write(f"{message.from_user.first_name} {email}\n")
    bot.send_message(message.chat.id, "Спасибо за предоставленную информацию. Ваш запрос был успешно сохранен.")


# Обработчик для кнопки "Отмена"
@bot.message_handler(func=lambda message: message.text == 'Отмена')
def cancel_action(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('✅ Получить ссылку на канал! ✅')
    btn2 = types.KeyboardButton('Анекдот дня')
    markup.row(btn1)
    markup.row(btn2)

    bot.send_message(message.chat.id, "Действие отменено.", reply_markup=markup)


bot.polling(none_stop=True)