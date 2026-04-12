from typing import Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(max_length=25)
    price: float = Field(ge=0)
    stock: float = Field(ge=0)
    category_id: int = Field(gt=0)


class ProductResponse(ProductBase):
    product_id: int = Field(ge=0)
    image_url: Optional[str] = None
