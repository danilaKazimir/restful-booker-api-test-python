from pydantic import RootModel


class HealthCheckResponse(RootModel[str]):
    pass
