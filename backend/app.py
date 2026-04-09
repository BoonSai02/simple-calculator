from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#  Allow frontend (important for browser requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalcInput(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {"message": "Calculator API is running..."}


@app.post("/add")
def add(data: CalcInput):
    return {"result": data.a + data.b}


@app.post("/sub")
def sub(data: CalcInput):
    return {"result": data.a - data.b}


@app.post("/mul")
def mul(data: CalcInput):
    return {"result": data.a * data.b}


@app.post("/div")
def div(data: CalcInput):
    # optional safe check
    if data.b == 0:
        return {"error": "Division by zero not allowed"}
    return {"result": data.a / data.b}


@app.post("/pow")
def power(data: CalcInput):
    return {"result": data.a ** data.b}