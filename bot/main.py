import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram_dialog import setup_dialogs
from bot.dialogs.sendChatEntity import message_dialog

bot = Bot(token="7802435259:AAGWXTJoVo1g-juinYsW_fQTPCOW9WEvWe8")
dp = Dispatcher()
dp.include_router(message_dialog)
bg_manager = setup_dialogs(dp)


@dp.message(CommandStart())
async def get_contact(message: types.Message):
    await message.answer(f"Logger works")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())