from fastapi import FastAPI
from src.routers import stores, sales

app = FastAPI()

app.include_router(stores.router)
app.include_router(sales.router)


@app.get("/")
async def root():
    return {"message": "Service is Running!"}


@app.get("/healthcheck", status_code=200)
def healthcheck():

    varenvs = [
        "VAR_ONE",
        "VAR_TWO"
    ]
    return {"varenv": "OK", "database": "OK"}


# OTHER FORMS
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#     tax: float
#
#
# class Items(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello Higor"}
#
#
# @app.post("/qrcode")
# async def qrcode(data):
#     print("Data: ", data)
#     return {"post": "ok"}
#     # return generate_qr_code(data)
#
#
# @app.post("/dados")
# async def dados(data: Item):
#     return {"Seu nome é ": data.name}
#
#
# @app.post("/vendas")
# async def vendas(request_venda: Vendas):
#     do_vendas(request_venda)
#
#
# # app.include_router(vendas, prefix="/vendas")
#
#
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[Union[str, None], Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
#
#
#
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: Union[str, None] = None,
#     item: Union[Items, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results