from typing import List

from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(default="Bearer")


class TokenDataSchema(BaseModel):
    scopes: List[str] = Field(default=[])
    doc_id: str = Field(...)
