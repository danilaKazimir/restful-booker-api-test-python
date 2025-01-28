from typing import Optional

from pydantic import BaseModel

from src.models.booking.booking_dates import BookingDates


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str]
