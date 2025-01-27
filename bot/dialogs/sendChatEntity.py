from typing import Any

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const, Case
from aiogram_dialog import Dialog, DialogManager
from bot.fsm.chat import ChatSG

from datetime import datetime

async def on_dialog_start(start_data: Any, manager: DialogManager):
    manager.dialog_data['telegram_id'] = start_data['telegram_id']
    manager.dialog_data['message'] = start_data['message']
    manager.dialog_data['timestamp'] = datetime.now().strftime('%d.%m.%Y %H:%M')

message_received_window = Window(
    Format(
           'От кого: {dialog_data[telegram_id]}\n'
           'Когда: {dialog_data[timestamp]}\n\n'
           'Сообщение: {dialog_data[message]}'),
    state=ChatSG.sendMessage
)

message_dialog = Dialog(
    message_received_window,
    on_start=on_dialog_start
)