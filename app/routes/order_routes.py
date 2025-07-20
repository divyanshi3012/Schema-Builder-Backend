from fastapi import APIRouter, status
from app.models.order import OrderModel
from app.database import order_collection
from app.utils import paginate
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderModel):
    order_dict = order.dict()
    order_collection.insert_one(order_dict)
    order_dict["_id"] = str(order_dict.get("_id", ""))
    return order_dict

@router.get("/orders/{user_id}", status_code=status.HTTP_200_OK)
def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = order_collection.find({"user_id": user_id}).sort("_id", 1)
    results = paginate(cursor, limit, offset)
    for o in results:
        o["_id"] = str(o["_id"])
    return results
