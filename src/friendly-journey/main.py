from fastapi import FastAPI

app = FastAPI(title="friendly-journey")

@app.get("/")
def health():
    return "`friendly-journey` is up and running"