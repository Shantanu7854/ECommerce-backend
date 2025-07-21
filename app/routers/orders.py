from fastapi import APIRouter
from app.models import OrderModel
from app.database import db
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: OrderModel):
    total = 0.0
    for item in order.items:
        product = await db.products.find_one({"_id": ObjectId(item.productId)})
        if product:
            total += product["price"] * item.qty

    order_dict = order.dict()
    order_dict["total"] = total
    result = await db.orders.insert_one(order_dict)
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = db.orders.find({"userId": user_id}).skip(offset).limit(limit)
    orders = []
    async for doc in cursor:
        items = []
        for item in doc["items"]:
            product = await db.products.find_one({"_id": ObjectId(item["productId"])})
            if product:
                
                items.append({
                    "productDetails": {
                        "name": product["name"],
                        "id": str(product["_id"])
                    },
                    "qty": item["qty"]
                })
        orders.append({
            "id": str(doc["_id"]),
            "items": items,
            "total": doc["total"]
        })

    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "limit": len(orders),
            "previous": offset - limit if offset - limit >= 0 else 0
        }
    }
