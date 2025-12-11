# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='DEAT ARC–NUR Stabilizer', version='0.2')

static_dir = "static"
# Mount statických souborů
app.mount("/static", StaticFiles(directory="static"), name="static")


# Serve editor.html from static folder
@app.get("/editor", include_in_schema=False)
def serve_editor():
    return FileResponse(os.path.join(static_dir, "editor.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

