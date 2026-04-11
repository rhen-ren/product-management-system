from fastapi import Form
from schema.product import ProductBase


def product_from_form(
    product_id: int = Form(...),
    name: str = Form(...),
    price: int = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...)
):

    return ProductBase(
        product_id=product_id,
        name=name,
        category_id=category_id,
        price=price,
        stock=stock,
    )
