from typing import Optional
from fastapi import APIRouter, File, Depends, UploadFile, Path
from fastapi.responses import JSONResponse
from schema.product import ProductBase
from services import product_service
from database.db import get_db
from dependency.get_product_from_form import product_from_form


router = APIRouter()


@router.get("/products", response_class=JSONResponse)
def get_products(db=Depends(get_db)):
    return product_service.get_products(db)


@router.get("/products/{product_id}", response_class=JSONResponse)
def get_product(product_id, db=Depends(get_db)):
    return product_service.get_product(product_id, db)


@router.post("/products", response_class=JSONResponse)
def create_product(product: dict, db=Depends(get_db)):
    return product_service.create_product(product, db)


@router.put("/products/{product_id_path}", response_class=JSONResponse)
def update_product(product_id_path: int = Path(...), image: Optional[UploadFile] = File(None),
                   product: ProductBase = Depends(product_from_form),
                   db=Depends(get_db)):
    return product_service.update_product(product_id_path, product, image, db)