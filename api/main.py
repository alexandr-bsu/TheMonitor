from fastapi import FastAPI
from chat.schema.ChatSchema import ChatUser, ChatEntity

import uvicorn
from aiogram_dialog import StartMode, ShowMode
from bot.main import bot
from bot.fsm.chat import ChatSG
from bot.main import bg_manager

app = FastAPI()

@app.post('/sendLogsMessage')
async def send_logs_entity(chat: ChatEntity, transmitter_id: int):
    manager = bg_manager.bg(bot, transmitter_id, transmitter_id, load=True)
    await manager.start(ChatSG.sendMessage, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
                        data={'chat': chat})

    return {'data': chat}

uvicorn.run(app, host='0.0.0.0', port=8080)