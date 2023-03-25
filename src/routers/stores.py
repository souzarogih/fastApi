from fastapi import Path, APIRouter
from typing import Annotated
from src.models.stores import Store

router = APIRouter(
    prefix="/store"
)


@router.get("/consult/{store_id}", tags=["stores"])
async def consult_store(store_id):
    print("Store: ", store_id)
    return {"content": f"Store {store_id}"}


@router.post("/create", tags=["stores"])
async def create_store(
        store_object: Annotated[Store, Path(title="Store products sales")]):
    print("Store data: ", store_object)
    return {"message": f"Store {store_object} criado com sucesso."}


@router.delete("/delete/{store_id}", tags=["stores"])
async def delete_store(store_id):
    print("Store data: ", store_id)
    return {"message": f"Store {store_id} removido com sucesso."}


@router.put("/create", tags=["stores"])
async def update_store(
        store_object: Store):
    print("Store data: ", store_object)
    return {"message": f"Store {store_object} atualizada com sucesso."}
