from pydantic import BaseModel

from src.models.booking.booking import Booking


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking
