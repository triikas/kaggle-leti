from aiogram import Bot, Dispatcher

waiting_rooms = {}
chat_rooms = {}

bot = Bot(token='7418313872:AAHWRvAjPdxX0J6UQe1RS-WrG-gPZreCW1U')
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=['join'])
async def join_room_handler(message):
    print(message.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)
