from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/confirm")
def confirt_payment(payload: dict):
    answer = dict()
    answer["code"] = 0
    answer["uid"] = payload.get("uid")
    answer["amount"] = payload.get("amount")
    print(answer)
    return answer

@app.post("/decline")
def decline_payment(payload: dict):
    answer = dict()
    answer["code"] = -1
    answer["uid"] = payload.get("uid")
    answer["amount"] = payload.get("amount")
    print(answer)
    return answer