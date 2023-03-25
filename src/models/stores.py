import uuid
from pydantic import BaseModel
from datetime import datetime as dt


class Store(BaseModel):
    store_name: str
    document_id: str
    store_type: str
