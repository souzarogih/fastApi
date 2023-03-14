from fastapi import FastAPI
from qrcode import generate_qr_code
from typing import Union
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.get("/")
async def root():
    return {"message": "Hello Higor"}


@app.post("/qrcode")
async def qrcode(data):
    print("Data: ", data)
    return {"post": "ok"}
    # return generate_qr_code(data)


@app.post("/dados")
async def dados(data: Item):
    return {"Seu nome é ": data.name}
