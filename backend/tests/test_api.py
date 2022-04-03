import pytest
from starlette.testclient import TestClient


class TestCount:
    def test_posts_and_counts_text(self, client: TestClient):
        response = client.post("/count", json={"text": "Zeit Medical"})
        assert response.status_code == 200
        payload = response.json()

        assert payload["a"] == 1
        assert payload["c"] == 1
        assert payload["d"] == 1
        assert payload["e"] == 2
        assert payload["i"] == 2
        assert payload["l"] == 1
        assert payload["m"] == 1
        assert payload["t"] == 1
        assert payload["z"] == 1

    def test_payload_contains_no_nonexistent_characters(self, client: TestClient):
        response = client.post("/count", json={"text": "Zeit Medical"})
        assert response.status_code == 200
        payload = response.json()

        with pytest.raises(KeyError):
            assert payload["Z"] == 0  # only lowercase letters

        with pytest.raises(KeyError):
            assert payload["x"] == 0  # no nonexistent letters, no error
