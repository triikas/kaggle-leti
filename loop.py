from aiogram import Bot, Dispatcher

waiting_rooms = {}
chat_rooms = {}


dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=['join'])
async def join_room_handler(message):
    print(message.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)
