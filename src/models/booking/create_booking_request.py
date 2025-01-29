from pydantic import BaseModel

from src.utils.faker_generate import FakerGenerate


class BookingDates(BaseModel):
    checkin: str = FakerGenerate.fake.date_between(start_date='-7d', end_date='-1d')
    checkout: str = FakerGenerate.fake.date_between(start_date='today', end_date='today')


class CreateBookingRequest(BaseModel):
    firstname: str = FakerGenerate.generate_first_name()
    lastname: str = FakerGenerate.generate_last_name()
    totalprice: int = FakerGenerate.generate_total_price()
    depositpaid: bool = FakerGenerate.generate_is_deposit_paid()
    bookingdates: BookingDates = BookingDates()
    additionalneeds: str = FakerGenerate.generate_additional_needs()
