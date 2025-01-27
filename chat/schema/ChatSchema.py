from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class ChatUser(BaseModel):
    role: Literal['client', 'admin'] = Field(default='client')
    name: str | None = Field(default=None)
    username: str | None = Field(default=None)
    id: int

class ChatEntity(BaseModel):
    sender: ChatUser
    message: str
    timestamp: datetime = Field(default=datetime.now())

