from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/get-address")
async def get_address(request: Request):
    print(request.client)

    request_body = await request.json()

    answer = dict()
    answer["code"] = 0
    answer["uid"] = request_body.get("uid")
    answer["amount"] = request_body.get("amount")
    print(answer)
    return answer

@app.post("/confirm")
def confirt_payment(payload: dict):
    print(payload)
    answer = dict()
    answer["code"] = 0
    answer["uid"] = payload.get("uid")
    answer["amount"] = payload.get("amount")
    print(answer)
    return answer

@app.post("/decline")
def decline_payment(payload: dict):
    print(payload)
    answer = dict()
    answer["code"] = -1
    answer["uid"] = payload.get("uid")
    answer["amount"] = payload.get("amount")
    print(answer)
    return answer