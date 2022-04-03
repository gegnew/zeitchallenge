from dataclasses import dataclass

from fastapi.exceptions import HTTPException
from starlette import status


@dataclass
class Errors:
    invalid_credentials_401 = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    document_not_found_404 = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not find document",
    )

    database_unavailable_503 = HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Database is not online",
    )
