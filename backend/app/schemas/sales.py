from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class SalesCreate(BaseModel):
    invoice_date: date
    invoice_number: str = Field(..., min_length=1, max_length=50)
    net_amount: float = Field(..., gt=0)
    total_amount: Optional[float] = None
    total_quantity: float = Field(..., gt=0)
    customer_code: Optional[str] = None
    customer_name: Optional[str] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    salesman_name: Optional[str] = None
    region_name: Optional[str] = None

class SalesUpdate(BaseModel):
    net_amount: Optional[float] = None
    total_quantity: Optional[float] = None

class SalesResponse(BaseModel):
    id: int
    invoice_date: date
    invoice_number: str
    net_amount: float
    total_quantity: float
    customer_name: Optional[str]
    product_name: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
