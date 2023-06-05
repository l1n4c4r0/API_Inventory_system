from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional[int] = None
    supplier_id : int = Field(ge=1, description="supplier.id")
    product_id : int  = Field(ge=1, description= "product.id")
    purchase_price : float = Field(ge=1,le=10000)
    class Config:
        schema_extra = {
            "example":{
                "supplier_id":2,
                "product_id":3,
                "purchase_price": 90000,
            }
        }