from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mistralai import Mistral
import os

API_KEY = os.getenv("MISTRAL_API_KEY")

if not API_KEY:
    raise RuntimeError("MISTRAL_API_KEY non défini !")

# On accepte la clé telle quelle (avec ou sans prefixe "mistral-")
app = FastAPI()
client = Mistral(api_key=API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Mistral Chat API is running "}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        response = client.chat.complete(
            model="mistral-tiny",
            messages=[{"role": "user", "content": req.message}]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API error occurred: {str(e)}")
