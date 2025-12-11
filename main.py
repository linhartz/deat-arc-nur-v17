from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Mount static directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Serve editor.html from static folder
@app.get("/editor", include_in_schema=False)
def serve_editor():
    return FileResponse(os.path.join(static_dir, "editor.html"))
