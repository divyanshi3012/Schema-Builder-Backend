from pydantic import BaseModel, Field
from typing import List

class ProductModel(BaseModel):
    name: str
    description: str
    price: float
    sizes: List[str] = Field(..., example=["small", "medium", "large"])
