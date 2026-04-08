import json

from fastapi import APIRouter, File, Form, Request, Depends, UploadFile
from fastapi.responses import JSONResponse
from services import productService
from database.db import get_db


router = APIRouter()

@router.get("/products", response_class=JSONResponse)
def getProducts(db = Depends(get_db)):
    return productService.getProducts(db)

@router.get("/products/{product_id}", response_class= JSONResponse)
def getProduct(product_id, db = Depends(get_db)):
    return productService.getProduct(product_id, db)

@router.post("/products", response_class= JSONResponse)
def createProduct(product: dict, db = Depends(get_db)):
    return productService.createProduct(product, db)

# FIXME: fix product service to handle uploaded images
@router.put("/products/{product_id}", response_class=JSONResponse)
def updateProduct(product_id, image: UploadFile = File(), product: str = Form(), db = Depends(get_db)):
    product = json.loads(product)
    return productService.updateProduct(product_id, product , db)