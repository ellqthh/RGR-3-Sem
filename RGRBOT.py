from telebot import types
import telebot;

bot = telebot.TeleBot('6960153732:AAFoiuI4BbQuecsP9mqRg_IW1TE1Q9l127A');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Здравствуй! Для дальнейшего взаимодействия напиши  /schedule   ")
    elif message.text == "/schedule":
        keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
        keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
        keyboard.add(key_no);
        question = 'Вот функции нашего приложения [https://6583-2a00-1fa3-631-6f18-5b3-8ec4-6dbc-58aa.ngrok-free.app/], они тебя устраивают?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    elif message.text == '/report':
        bot.send_message(message.from_user.id, "Напиши пожалуйста номер того, что тебя не устраивает.");
    elif message.text == '1' or '2' or '3' or '4':
        bot.send_message(message.from_user.id, 'Я зафиксировал и отправил твои пожелания разработчику.');
        bot.reply_to(message, "Этот пункт не устраивает пользователя.");
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /schedule.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            bot.send_message(call.message.chat.id, 'Отлично! Я отправлю твой ответ разработчику.');
            bot.send_message(1944402724, 'Пользователя устраивает расписание');
        elif call.data == "no":
            ...
            bot.send_message(call.message.chat.id, 'Напиши команду /report')


bot.polling(none_stop=True, interval=0)