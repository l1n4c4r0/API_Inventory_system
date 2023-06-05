from pydantic import BaseModel, Field
from typing import Optional

class Supplier(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=30,min_length=3)
    addrees : str = Field(max_length=30,min_length=3,ge=0,le=1000)
    phone : int = Field(ge=1,le=1000)
    email : str = Field(max_length=30,min_length=3)

    class Config:
        schema_extra = {
            "example":{
                "id":2,
                "name": 'Beauty',
                "addrees": '65 street number 12',
                "phone": 552387,
                "email": 'beautycompany@email.com',
            }
        }