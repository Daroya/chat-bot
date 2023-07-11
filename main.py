import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token='Token_Bot')
dp = Dispatcher()


@dp.message(Command('rules'))
async def rules(message: types.Message):
    await message.answer('''Rules in chat''')

@dp.message(Command('infobot'))
async def info(message: types.Message):
    await message.answer('''information about bota''')

@dp.message(Command('ban'))
async def ban_user(message: types.Message):
    if message.reply_to_message is None:
        await message.answer("This command must be used when replying to a user's message.")
        return
    user_id = message.reply_to_message.from_user.id
    await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.answer(f"User from ID {user_id} was banned!")

@dp.message(Command('unban'))
async def unban_user(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.answer(f"User from ID {user_id} was unbanned!")

@dp.message(Command('admincommand'))
async def info(message: types.Message):
    await message.answer('''🛑Command for admin🛑
    ------------------------------------
    /ban - banned people
    /unban - unbanned people''')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
