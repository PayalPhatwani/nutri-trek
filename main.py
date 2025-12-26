from fastapi import FastAPI
# from config import settings
from api.v1.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "Nutri-Trek API is running"}
