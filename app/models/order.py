from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderModel(BaseModel):
    user_id: str
    items: List[OrderItem]
