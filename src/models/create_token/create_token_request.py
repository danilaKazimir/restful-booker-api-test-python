from typing import Optional

from pydantic import BaseModel


class CreateTokenRequest(BaseModel):
    username: Optional[str]
    password: Optional[str]
