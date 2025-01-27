from aiogram.filters.state import StatesGroup, State

class ChatSG(StatesGroup):
    sendMessage = State()
