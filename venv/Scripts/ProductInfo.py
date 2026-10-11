from pydantic import BaseModel

class ProductInfo(BaseModel):
    product: float 
    quantity: float 
    unit_price: float 
    department: str
    city: str
    payment_method: str
    