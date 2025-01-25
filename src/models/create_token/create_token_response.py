from pydantic import BaseModel


class CreateTokenValidResponse(BaseModel):
    token: str


class CreateTokenInvalidResponse(BaseModel):
    reason: str
