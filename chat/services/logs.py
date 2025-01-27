from chat.schema.ChatSchema import ChatEntity

class Receiver:
    async def send(self, entity: ChatEntity, transmitter):
        pass

    async def broadcast(self, entity: ChatEntity):
        pass

class TelegramReceiver(Receiver):
    def __init__(self, token):
        self.token = token

    async def send(self, entity: ChatEntity, transmitter_id: int):
        pass


class Logs:
    @staticmethod
    async def send_log_message(receiver: Receiver, entity: ChatEntity):
        response = receiver.send(entity)
        return response

    async def gather_logs(self):
        pass




