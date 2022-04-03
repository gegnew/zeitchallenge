from datetime import datetime, timedelta
from typing import List
from fastapi.security import SecurityScopes

from app.config import app_settings
from jose import jwt, JWTError

from app.schemas import TokenDataSchema


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = (
        datetime.utcnow() + expires_delta
        or app_settings.FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        app_settings.FASTAPI_SECRET_KEY,
        algorithm=app_settings.FASTAPI_HASH_ALGORITHM,
    )
    return encoded_jwt


def verify_scopes(
    security_scopes: SecurityScopes,
    token_scopes: List[str],
):
    if not set(security_scopes.scopes).issubset(set(token_scopes)):
        raise app_settings.errors.invalid_credentials_401


def decode_token(token: str) -> TokenDataSchema:
    try:
        payload = jwt.decode(
            token,
            app_settings.FASTAPI_SECRET_KEY,
            algorithms=[app_settings.FASTAPI_HASH_ALGORITHM],
        )

        doc_id: str = payload.get("doc_id", None)
        token_scopes = payload.get("scopes", [])

        if doc_id is None:
            raise app_settings.errors.invalid_credentials_401

        token_data = TokenDataSchema(scopes=token_scopes, doc_id=doc_id)

    except JWTError:
        raise app_settings.errors.invalid_credentials_401

    return token_data
