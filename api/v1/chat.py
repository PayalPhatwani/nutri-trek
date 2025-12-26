from fastapi import APIRouter
from models.chat import ChatMessage
from services.nutrition import analyze_food_text

router = APIRouter()

@router.post("/chat")
def chat(msg: ChatMessage):
    nutrition = analyze_food_text(msg.message)

    return {
        "input": msg.message,
        "nutrition": nutrition
    }
