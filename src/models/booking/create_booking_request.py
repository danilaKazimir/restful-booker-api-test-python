from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str = '2018-01-01'
    checkout: str = '2019-01-01'


class CreateBookingRequest(BaseModel):
    firstname: str = 'Jim'
    lastname: str = 'Brown'
    totalprice: int = 111
    depositpaid: bool = True
    bookingdates: BookingDates = BookingDates()
    additionalneeds: str = 'Breakfast'
