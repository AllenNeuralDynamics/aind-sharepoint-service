"""Tests for handler module"""

import pytest
from unittest.mock import MagicMock
from aind_sharepoint_service_server.handler import SessionHandler
from fastapi.testclient import TestClient
from aind_sharepoint_service_server.models import LASList
from aind_sharepoint_service_server.client import SharePointClient
from aind_sharepoint_service_server.configs import Settings
class TestSessionHandler:
    """Test SessionHandler"""

    def test_get_las_2020_procedures(self, mock_las2020: MagicMock, client: TestClient):
        """Test get_las_2020_procedures method"""
        settings = Settings()
        test_client = SharePointClient.from_settings(settings=settings)
        handler = SessionHandler(session=test_client)
        subject_id = "000000"
        results = handler.get_las_2020_procedures(subject_id)
        assert isinstance(results, list)
        assert len(results) > 0
        assert all(isinstance(item, LASList) for item in results)

if __name__ == "__main__":
    pytest.main([__file__])
