from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://my-ollama-service:11434"

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/chat")
def chat(prompt: str):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return {"response": response.json()["response"]}
