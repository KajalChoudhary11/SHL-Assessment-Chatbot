from fastapi import APIRouter
from APP.dtos import ChatRequest
from APP.services import process_chat

router = APIRouter()


@router.get("/health")
def health():

    return {"status": "ok"}

@router.post("/chat")
def chat(request: ChatRequest):

    return process_chat(request.messages)