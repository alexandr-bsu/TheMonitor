from typing import Any

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const, Case
from aiogram_dialog import Dialog, DialogManager
from bot.fsm.chat import ChatSG

async def on_dialog_start(start_data: Any, manager: DialogManager):
    chat = start_data['chat']
    manager.dialog_data['sender'] = chat.sender
    manager.dialog_data['message'] = chat.message
    manager.dialog_data['timestamp'] = chat.timestamp.strftime('%d.%m.%Y %H:%M')

message_received_window = Window(
    Format('Пришло новое сообщение [{dialog_data[sender].role}]:\n'
           'От кого: {dialog_data[sender].name} ({dialog_data[sender].id})\n'
           'Когда: {dialog_data[timestamp]}\n\n'
           'Сообщение: {dialog_data[message]}'),
    state=ChatSG.sendMessage
)

message_dialog = Dialog(
    message_received_window,
    on_start=on_dialog_start
)