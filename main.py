<<<<<<< HEAD
# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

# Mount statických souborů
app.mount("/static", StaticFiles(directory="static"), name="static")

=======
import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
>>>>>>> b869dc05de23679ba3a744b0880d4809e3253796

# Mount statických souborů
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# /editor endpoint
@app.get("/editor", include_in_schema=False)
def serve_editor():
<<<<<<< HEAD
    return FileResponse(os.path.join(static_dir, "editor.html"))

from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("WS: Connected")
    try:
        while True:
            msg = await ws.receive_text()
            await ws.send_text(f"Echo: {msg}")
    except Exception:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


=======
    editor_path = os.path.join(STATIC_DIR, "editor.html")
    return FileResponse(editor_path)


# ------------------------
# WebSocket manager
# ------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def broadcast(self, message: str):
        living = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
                living.append(connection)
            except RuntimeError:
                pass
        self.active_connections = living

manager = ConnectionManager()

@app.websocket("/ws/nur")
async def websocket_nur(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            payload = await websocket.receive_text()
            await websocket.send_text(f"Echo: {payload}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# ------------------------
# Lokální run
# ------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
>>>>>>> b869dc05de23679ba3a744b0880d4809e3253796
