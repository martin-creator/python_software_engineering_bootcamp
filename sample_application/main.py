from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def home():
    return {"message": "Hello, World"}

@app.get("/test", response_class=PlainTextResponse)
def test_endpoint():
    return "Mic check 1, 2, 3..."