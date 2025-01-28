from pydantic import BaseModel, RootModel

from src.models.booking.booking import Booking


class CreateBookingValidResponse(BaseModel):
    bookingid: int
    booking: Booking


class CreateBookingInvalidResponse(RootModel[str]):
    pass
