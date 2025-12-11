from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
import asyncio
import json
import math
import statistics

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve editor.html from static folder
@app.get("/editor", include_in_schema=False)
def serve_editor():
    return FileResponse(os.path.join(static_dir, "editor.html"))
