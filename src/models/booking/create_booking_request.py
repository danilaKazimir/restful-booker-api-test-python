from pydantic import BaseModel, Field

from src.utils.faker_generate import FakerGenerate


class BookingDates(BaseModel):
    checkin: str = Field(default_factory=lambda: FakerGenerate.generate_date(start_date='-7d', end_date='-3d'))
    checkout: str = Field(default_factory=lambda: FakerGenerate.generate_date(start_date='today', end_date='today'))


class CreateBookingRequest(BaseModel):
    firstname: str = Field(default_factory=FakerGenerate.generate_first_name)
    lastname: str = Field(default_factory=FakerGenerate.generate_last_name)
    totalprice: int = Field(default_factory=FakerGenerate.generate_total_price)
    depositpaid: bool = Field(default_factory=FakerGenerate.generate_is_deposit_paid)
    bookingdates: BookingDates = Field(default_factory=BookingDates)
    additionalneeds: str = Field(default_factory=FakerGenerate.generate_additional_needs)
