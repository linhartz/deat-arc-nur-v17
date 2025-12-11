# main.py
import os
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

static_dir = "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/editor", include_in_schema=False)
def serve_editor():
    path = os.path.join(static_dir, "editor.html")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"{path} not found")
    return FileResponse(path)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

