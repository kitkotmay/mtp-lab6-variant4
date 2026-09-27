from fastapi import FastAPI


app = FastAPI(
    title="Hello API",
    description="Лабораторная работа №6",
)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
