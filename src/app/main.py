import uvicorn
from fastapi import FastAPI

from src.app.routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users")


@app.get("/")
def health():
    return "`app` is up and running"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
