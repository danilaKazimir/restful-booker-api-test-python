from typing import Optional

from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: Optional[str] = None
    checkout: Optional[str] = None
