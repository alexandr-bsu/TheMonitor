from fastapi import FastAPI, Body
from chat.schema.ChatSchema import ChatUser, ChatEntity
from typing import Annotated
import uvicorn
from aiogram_dialog import StartMode, ShowMode
from bot.main import bot
from bot.fsm.chat import ChatSG
from bot.main import bg_manager
import json

app = FastAPI()

@app.post('/sendLogsMessage')
async def send_logs_entity(telegram_id:Annotated[int, Body()], message: Annotated[str,  Body()], transmitter_id: int):
    manager = bg_manager.bg(bot, transmitter_id, transmitter_id, load=True)
    await manager.start(ChatSG.sendMessage, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
                         data={'telegram_id': telegram_id, 'message': message})

    return {'data':
        {'telegram_id': telegram_id, 'message': message}
    }

uvicorn.run(app, port=8080)