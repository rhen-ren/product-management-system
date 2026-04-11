from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_id: int = Field(min_length=1)
    name: str = Field(max_length=25)
    price: int = Field(ge=0)
    stock: int = Field(ge=0)
    category_id: int = Field(gt=0)
    category_name: str = Field(min_length=1)
