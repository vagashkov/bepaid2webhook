from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def process_message(payload: dict):
    answer = dict()
    answer["code"] = 0
    answer["uid"] = payload.get("uid")
    answer["amount"] = payload.get("amount")
    print(answer)
    return answer
