from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"hi ,polina server is working"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
