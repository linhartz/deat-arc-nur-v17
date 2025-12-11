from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import os

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

# Mount static directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount('/static', StaticFiles(directory="static"), name="static")

# Serve editor.html from static folder
@app.get("/editor", include_in_schema=False)
def serve_editor():
    return FileResponse(os.path.join(static_dir, "editor.html"))
