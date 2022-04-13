from typing import Generator

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="class")
def client(request) -> Generator:
    """Customizeable client scoped to a test class"""
    with TestClient(app) as client:
        yield client
