from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str
