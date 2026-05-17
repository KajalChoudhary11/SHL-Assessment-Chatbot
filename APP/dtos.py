from pydantic import BaseModel
from typing import List

class Messagae(BaseModel):
    role: str
    content:str

class ChatRequest(BaseModel):
    messages: List[Messagae]
