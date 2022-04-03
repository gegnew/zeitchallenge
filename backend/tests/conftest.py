import pytest
from starlette.testclient import TestClient

from app.config.settings import build_settings_object
from app.main import get_app


def get_test_client(
    app_settings=build_settings_object(),
) -> TestClient:
    app = get_app(app_settings or build_settings_object())
    return TestClient(app)


@pytest.fixture(scope="class")
def client(request) -> TestClient:
    """Customizeable client scoped to a test class"""
    kwargs = dict(
        app_settings=getattr(request.cls, "app_settings", None),
    )
    return get_test_client(**{k: v for k, v in kwargs.items() if v is not None})
