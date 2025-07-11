from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def status_check():
    return {"status" : "ok"}
