from datetime import timedelta
import os

from jose import jwt

from app.api.endpoints.auth import create_access_token, decode_token
from app.schemas.token_schema import TokenDataSchema


def test_creates_new_jwt():
    data = {"user": 1}
    expires = timedelta(1)
    token = create_access_token(data, expires)
    assert jwt.get_unverified_claims(token)["user"] == 1
    assert jwt.get_unverified_headers(token) == {"alg": "HS256", "typ": "JWT"}


def test_decodes_token_with_secret_key():
    # Given: a token created with a secret key
    os.environ["FASTAPI_SECRET_KEY"] = "foobarbaz"
    data = {"user": 1, "doc_id": 1, "scopes": ["test"]}
    expires = timedelta(1)
    token = create_access_token(data, expires)

    # When: it is decoded with the same key
    payload = decode_token(token)

    # Then: it returns an instance of a pydantic model
    assert type(payload) is TokenDataSchema
    assert payload.doc_id == "1"
    assert payload.dict() == {"scopes": ["test"], "doc_id": "1"}
