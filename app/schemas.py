from pydantic import BaseModel
from typing import List, Dict, Any

class ProductOut(BaseModel):
    id: str
    name: str
    price: float

class OrderOut(BaseModel):
    id: str
    items: List[Dict[str, Any]]
    total: float
