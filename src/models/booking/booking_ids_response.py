from pydantic import BaseModel, RootModel
from typing import List


class BookingId(BaseModel):
    bookingid: int


class BookingIdsResponse(RootModel[List[BookingId]]):
    pass
