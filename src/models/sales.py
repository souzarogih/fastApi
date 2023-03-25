from pydantic import BaseModel


class Sales(BaseModel):
    produto: list
    price: float
    tax: float


def makes_sales(request_vendas):
    print("Chegou request")
    print(request_vendas)
    print(type(request_vendas))
    # print(request_vendas["produto"])
    # print(request_vendas["description"])
    # print(request_vendas["price"])
    # print(request_vendas["tax"])
