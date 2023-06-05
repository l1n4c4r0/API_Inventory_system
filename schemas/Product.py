from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=20,min_length=2)
    brand : str = Field(max_length=20,min_length=2)
    description : str = Field(max_length=20,min_length=2)
    price : float = Field(ge=1,le=10000000)
    entry_date : int = Field(ge=1,le=10000000)
    availability : str = Field(max_length=20,min_length=2)
    available_quantity : int = Field(ge=1,le=1000)
    
    class Config:
        schema_extra = {
            "example":{
                "id": 1,
                "name": 'boots',
                "brand": 'nata',
                "description": 'black color',
                "price": 80000,
                "entry_date": 20230206,
                "availability": 'yes',
                "available_quantity": 6,
            }
        }