from fastapi import APIRouter, status, Query
from app.models.product import ProductModel
from app.database import product_collection
from app.utils import paginate
from bson import ObjectId
import re

router = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductModel):
    product_dict = product.dict()
    product_collection.insert_one(product_dict)
    product_dict["_id"] = str(product_dict.get("_id", ""))
    return product_dict

@router.get("/products", status_code=status.HTTP_200_OK)
def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["sizes"] = size

    cursor = product_collection.find(query).sort("_id", 1)
    results = paginate(cursor, limit, offset)
    for p in results:
        p["_id"] = str(p["_id"])
    return results
