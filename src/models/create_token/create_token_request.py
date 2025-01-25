from pydantic import BaseModel


class CreateTokenRequest(BaseModel):
    username: str = None
    password: str = None
