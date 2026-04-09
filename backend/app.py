from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalcInput(BaseModel):
    a: float
    b: float

@app.get("/")
def home():
    return {
        "message": "Calculator API is running..."
    }

@app.post("/add")
def add(data: CalcInput):
    return {
        "result": data.a + data.b
    }

@app.post("/sub")
def sub(data: CalcInput):
    return {
        "result": data.a - data.b
    }
@app.post("/mult")
def mult(data: CalcInput):
    return {
        "result": data.a * data.b
    }

@app.post("/div")
def div(data: CalcInput):
    return {
        "result": data.a / data.b
    }

@app.post("/pow")
def pow(data: CalcInput):
    return {
        "result": data.a ** data.b
    }


