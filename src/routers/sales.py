from fastapi import Path, APIRouter
from typing import Annotated
from src.models.sales import Sales

router = APIRouter(
    prefix="/sale"
)


@router.get("/listsales/{store_id}", tags=["sale"])
async def consult_sales_for_store(store_id):
    print("Store: ", store_id)
    return {"content": f"Store {store_id}"}


@router.get("/consult/{sale_id}", tags=["sale"])
async def consult_store(sale_id):
    print("Sale: ", sale_id)
    return {"content": f"Sale {sale_id}"}


@router.post("/create", tags=["sale"])
async def create_store(
        sale_object: Annotated[Sales, Path(title="Store products sales")]):
    print("Sale data: ", sale_object)
    return {"message": f"Sale {sale_object} criado com sucesso."}


@router.delete("/delete/{sale_id}", tags=["sale"])
async def delete_store(sale_id):
    print("Store data: ", sale_id)
    return {"message": f"Sale {sale_id} removido com sucesso."}


@router.put("/create", tags=["sale"])
async def update_store(
        store_object: Sales):
    print("Sale data: ", store_object)
    return {"message": f"Sale {store_object} atualizada com sucesso."}
