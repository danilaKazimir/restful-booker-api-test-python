from pydantic import BaseModel

from src.models.booking.booking import Booking


class CreateBookingValidResponse(BaseModel):
    bookingid: int
    booking: Booking
