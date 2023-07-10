import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token='6066687635:AAF9PXNl1PiAd471gIP3xy4oDb4wKiureGw')
dp = Dispatcher()


@dp.message(Command('rules'))
async def rules(message: types.Message):
    await message.answer('''👮️Правила 7-А класу!
------------------------------------------
1. Дотримуватись правил пристойності та лексики.
2. Не турбуйте Один Одного по дрібницях.
3. Не ображайте один одного
4. Не принижуй інших.
5. Не вирішуйте у спільних чатах приватні питання.
6. Будьте ввічливі з усіма учасниками чату.
7. Заборонено Спамити в Групі (флуд, флейм).
8. Заборонено говорити про Расизм та уникати суржика.‍👮️''')

@dp.message(Command('infobot'))
async def info(message: types.Message):
    await message.answer('''🛑Інформація про команди бота!
------------------------------------------
/rules - правила чату
/infobot - інформація команд бота
/main - хто на данний момент староста/замісник класу\n
Скоро можут бути обновлення команд!🛑''')

@dp.message(Command('main'))
async def info(message: types.Message):
    await message.answer('''Староста/Зам
------------------------------------------
На данний момент\n
Староста - ?
-------------------------
Замісник - ?''')



@dp.message(Command('ban'))
async def ban_user(message: types.Message):
    if message.reply_to_message is None:
        await message.answer("Цю команду потрібно використовувати, відповідаючи на повідомлення користувача.")
        return
    user_id = message.reply_to_message.from_user.id
    await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.answer(f"Користувач з ID {user_id} був забанений!")

@dp.message(Command('unban'))
async def unban_user(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
    await message.answer(f"Користувач з ID {user_id} був розбанений!")

@dp.message(Command('admincommand'))
async def info(message: types.Message):
    await message.answer('''🛑Команди для адміністраторів!🛑
    ------------------------------------
    /ban - забанити людину
    /unban - розбанити людину!''')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
