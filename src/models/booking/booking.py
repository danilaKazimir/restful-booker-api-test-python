from typing import Optional

from pydantic import BaseModel

from src.models.booking.booking_dates import BookingDates
from src.utils.faker_generate import FakerGenerate


class Booking(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    totalprice: Optional[int] = None
    depositpaid: Optional[bool] = None
    bookingdates: Optional[BookingDates] = None
    additionalneeds: Optional[str] = None

    def fill_data(self, full_data: bool = True, fields: Optional[list[str]] = None) -> "Booking":
        if full_data:
            self.firstname = FakerGenerate.generate_first_name()
            self.lastname = FakerGenerate.generate_last_name()
            self.totalprice = FakerGenerate.generate_total_price()
            self.depositpaid = FakerGenerate.generate_is_deposit_paid()
            self.bookingdates = BookingDates(
                checkin=FakerGenerate.generate_date(start_date='-10d', end_date='-5d'),
                checkout=FakerGenerate.generate_date(start_date='-3d', end_date='today')
            )
            self.additionalneeds = FakerGenerate.generate_additional_needs()

        if fields:
            for field in fields:
                match field:
                    case 'firstname':
                        self.firstname = FakerGenerate.generate_first_name()
                    case 'lastname':
                        self.lastname = FakerGenerate.generate_last_name()
                    case 'totalprice':
                        self.totalprice = FakerGenerate.generate_total_price()
                    case 'depositpaid':
                        self.depositpaid = FakerGenerate.generate_is_deposit_paid()
                    case 'checkin':
                        if not self.bookingdates:
                            self.bookingdates = BookingDates()
                        self.bookingdates.checkin = FakerGenerate.generate_date(start_date='-10d', end_date='-5d')
                    case 'checkout':
                        if not self.bookingdates:
                            self.bookingdates = BookingDates()
                        self.bookingdates.checkout = FakerGenerate.generate_date(start_date='-3d', end_date='today')
                    case 'additionalneeds':
                        self.additionalneeds = FakerGenerate.generate_additional_needs()
                    case _:
                        raise ValueError('Incorrect value provided!')

        if full_data and fields:
            raise ValueError('You can use only full_data attribute or fields attribute! \
                If you want to use fields attribute, please fill full_data = False')

        return self
