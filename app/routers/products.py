from fastapi import APIRouter, Query
from app.database import db
from app.models import ProductModel
from bson import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductModel):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products")
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc["name"],
            "price": doc["price"]
        })

    return {
        "data": products,
        "page": {
            "next": offset + limit,
            "limit": len(products),
            "previous": offset - limit if offset - limit >= 0 else 0
        }
    }
