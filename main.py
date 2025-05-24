from datetime import datetime
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Set default port
port = int(os.getenv("PORT", 8000))

# Create FastAPI instance
app = FastAPI(
    title="FastAPI Demo",
    description="A demo FastAPI application for Blossom deployment",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Models
class EchoRequest(BaseModel):
    message: str

# Routes
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/api/hello")
async def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.post("/api/echo")
async def echo(data: EchoRequest):
    return {
        "message": "Echo response",
        "received": data.dict(),
        "timestamp": datetime.utcnow().isoformat()
    }
