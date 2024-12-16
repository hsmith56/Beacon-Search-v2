from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}