import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

# Statické soubory
static_dir = "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# /editor endpoint
@app.get("/editor", include_in_schema=False)
def serve_editor():
    editor_path = os.path.join(static_dir, "editor.html")
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
