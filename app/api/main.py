from fastapi import FastAPI
from app.api import upload, chat

app = FastAPI()

@app.get("/")
def read_root():
    # The function below the decorator handles the request
    return {"Hello": "World"}

app.include_router(upload.router)
app.include_router(chat.router)
