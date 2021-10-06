from fastapi import FastAPI
app = FastAPI()

@app.get("/ping", summary="Get a message json" ,status_code=200)
def hello(
    name: str = "pong",
):

    return {"message": name}
