from pydantic import RootModel


class GetBookingNotFoundResponse(RootModel[str]):
    pass
