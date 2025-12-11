# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

# Mount statických souborů
app.mount("/static", StaticFiles(directory="static"), name="static")



# Serve editor.html from static folder
@app.get("/editor", include_in_schema=False)
def serve_editor():
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


