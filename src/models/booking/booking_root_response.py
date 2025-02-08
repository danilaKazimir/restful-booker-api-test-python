from pydantic import RootModel


class BookingRootResponse(RootModel[str]):
    pass
