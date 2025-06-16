"""Test routes"""

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient


class TestHealthcheckRoute:
    """Test healthcheck responses."""

    def test_get_health(self, client):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]

    def test_get_200_las2020_procedures(
        self, client: TestClient, mock_las2020: MagicMock
    ):
        """Tests get_las2020_procedures endpoint"""
        response = client.get("/las2020_procedures/000000")
        assert 200 == response.status_code
        data = response.json()
        assert len(data) == 4

    def test_get_404_las2020_procedures(
        self, client: TestClient, mock_las2020: MagicMock
    ):
        """Tests get_las2020_procedures endpoint with no data"""
        response = client.get("/las2020_procedures/999999")
        assert 404 == response.status_code
        assert (
            "No procedures found for subject ID 999999 in LAS 2020."
            == response.json()["detail"]
        )


if __name__ == "__main__":
    pytest.main([__file__])
