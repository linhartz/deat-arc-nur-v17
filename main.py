# main.py
import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Mount statických souborů
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# /editor endpoint
@app.get("/editor", include_in_schema=False)
def serve_editor():
    editor_path = os.path.join(STATIC_DIR, "editor.html")
    if not os.path.exists(editor_path):
        return {"error": "editor.html not found in static folder"}
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
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        living = []
        for conn in self.active_connections:
            try:
                await conn.send_text(message)
                living.append(conn)
            except Exception:
                pass
        self.active_connections = living

manager = ConnectionManager()

@app.websocket("/ws/nur")
async def websocket_nur(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            payload = await websocket.receive_text()
            # echo payload zpět klientovi
            await websocket.send_text(f"Echo: {payload}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# ------------------------
# Lokální run / Railway port
# ------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
