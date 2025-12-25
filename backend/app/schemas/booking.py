from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.booking import BookingStatus

class BookingBase(BaseModel):
    service_id: int
    start_time: datetime
    notes: Optional[str] = None

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    customer_id: int
    end_time: datetime
    status: BookingStatus
    created_at: datetime
    
    class Config:
        from_attributes = True
