from fastapi import FastAPI, Request
import uvicorn
import json

app = FastAPI()

VERIFY_TOKEN = 'YOUR_VERIFY_TOKEN'

@app.get("/")
async def verify(request: Request):
    hub_mode = request.query_params.get("hub.mode")
    hub_challenge = request.query_params.get("hub.challenge")
    hub_verify_token = request.query_params.get("hub.verify_token")

    if hub_mode == "subscribe" and hub_challenge:
        if hub_verify_token == VERIFY_TOKEN:
            return int(hub_challenge)
        return {"error": "Verification token mismatch"}, 403
    return {"message": "Hello world"}

@app.post("/")
async def webhook(request: Request):
    body = await request.json()
    print(json.dumps(body, indent=2))
    # Handle the received message here
    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
