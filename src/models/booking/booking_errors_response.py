from pydantic import RootModel


class BookingErrorsResponse(RootModel[str]):
    pass
