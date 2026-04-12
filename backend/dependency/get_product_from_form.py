from fastapi import Form
from schema.product import ProductBase


def product_from_form(
    name: str = Form(...),
    price: int = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...)
):

    return ProductBase(
        name=name,
        category_id=category_id,
        price=price,
        stock=stock,
    )
