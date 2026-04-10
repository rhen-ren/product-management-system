import json

from fastapi import APIRouter, File, Form, Request, Depends, UploadFile
from fastapi.responses import JSONResponse
from services import product_service
from database.db import get_db


router = APIRouter()

@router.get("/products", response_class=JSONResponse)
def get_products(db = Depends(get_db)):
    return product_service.getProducts(db)

@router.get("/products/{product_id}", response_class= JSONResponse)
def get_product(product_id, db = Depends(get_db)):
    return product_service.getProduct(product_id, db)

@router.post("/products", response_class= JSONResponse)
def create_product(product: dict, db = Depends(get_db)):
    return product_service.createProduct(product, db)

@router.put("/products/{product_id}", response_class=JSONResponse)
def update_product(product_id, image: UploadFile = File(), product: str = Form(), db = Depends(get_db)):
    product = json.loads(product)
    return product_service.updateProduct(product_id, product, image , db)