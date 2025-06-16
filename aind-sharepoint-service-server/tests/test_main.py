"""Module to test main app"""

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient


class TestMain:
    """Tests app endpoints"""

    def test_get_healthcheck(self, client):
        """Tests healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    def test_get_las2020_procedures(
        self, client: TestClient, mock_las2020: MagicMock
    ):
        """Tests get_las2020_procedures endpoint"""
        response = client.get("/las2020_procedures/000000")
        assert 200 == response.status_code
        data = response.json()
        assert len(data) == 4


if __name__ == "__main__":
    pytest.main([__file__])
