"""Test routes"""

from typing import Any, Dict, List
from unittest.mock import MagicMock, call, patch

import pytest
from azure.core.credentials import AccessToken
from fastapi.testclient import TestClient

from aind_sharepoint_service_server.configs import Settings
from aind_sharepoint_service_server.route import (
    get_access_token,
    get_las_2020_list,
    get_nsb_2019_list,
    get_nsb_2023_list,
    get_nsb_present_list,
)


@pytest.mark.asyncio
class TestRoute:
    """Test Routes."""

    async def test_get_health(self, client: TestClient):
        """Tests a good response"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]

    @patch("aind_sharepoint_service_server.route.ClientSecretCredential")
    async def test_get_access_token(self, mock_azure_credentials: MagicMock):
        """Tests get_access_token method"""
        mock_azure_credentials.return_value.get_token.return_value = (
            AccessToken(token="abc", expires_on=100)
        )
        token = await get_access_token(settings=Settings())
        mock_azure_credentials.assert_has_calls(
            [
                call(
                    tenant_id="tenant_id",
                    client_id="client_id",
                    client_secret="client_secret",
                ),
                call().get_token("https://graph.microsoft.com/.default"),
            ]
        )
        assert "abc" == token

    @patch("aind_sharepoint_service_server.route.get_access_token")
    @patch(
        "aind_sharepoint_service_server.handler.SessionHandler.get_list_items"
    )
    @patch("aind_sharepoint_service_server.route.AsyncClient")
    async def test_get_las_2020_list(
        self,
        mock_client: MagicMock,
        mock_get_list_items: MagicMock,
        mock_get_access_token: MagicMock,
        mock_get_las_2020_list_items: List[Dict[str, Any]],
    ):
        """Tests get_las_2020_list method"""
        mock_get_access_token.return_value = "abc"
        mock_get_list_items.return_value = mock_get_las_2020_list_items
        list_items = await get_las_2020_list(settings=Settings())
        mock_client.assert_called_once()
        assert 4 == len(list_items)

    @patch("aind_sharepoint_service_server.route.get_las_2020_list")
    async def test_get_las_2020(
        self,
        mock_get_las_2020_list: MagicMock,
        client: TestClient,
        mock_get_las_2020_list_items: List[Dict[str, Any]],
    ):
        """Tests get_las_2020 route"""
        mock_get_las_2020_list.return_value = mock_get_las_2020_list_items
        response = client.get("/las_2020/797823")
        assert 200 == response.status_code
        assert 1 == len(response.json())

    @patch("aind_sharepoint_service_server.route.get_access_token")
    @patch(
        "aind_sharepoint_service_server.handler.SessionHandler.get_list_items"
    )
    @patch("aind_sharepoint_service_server.route.AsyncClient")
    async def test_get_nsb_2023_list(
        self,
        mock_client: MagicMock,
        mock_get_list_items: MagicMock,
        mock_get_access_token: MagicMock,
        mock_get_nsb_2023_list_items: List[Dict[str, Any]],
    ):
        """Tests get_las_2020_list method"""
        mock_get_access_token.return_value = "abc"
        mock_get_list_items.return_value = mock_get_nsb_2023_list_items
        list_items = await get_nsb_2023_list(
            settings=Settings(), subject_id="657849"
        )
        mock_client.assert_called_once()
        assert 1 == len(list_items)

    @patch("aind_sharepoint_service_server.route.get_nsb_2023_list")
    async def test_get_nsb_2023(
        self,
        mock_get_nsb_2023_list: MagicMock,
        client: TestClient,
        mock_get_nsb_2023_list_items: List[Dict[str, Any]],
    ):
        """Tests get_nsb_2023 route"""
        mock_get_nsb_2023_list.return_value = mock_get_nsb_2023_list_items
        response = client.get("/nsb_2023/657849")
        assert 200 == response.status_code
        assert 1 == len(response.json())

    @patch("aind_sharepoint_service_server.route.get_access_token")
    @patch(
        "aind_sharepoint_service_server.handler.SessionHandler.get_list_items"
    )
    @patch("aind_sharepoint_service_server.route.AsyncClient")
    async def test_get_nsb_2019_list(
        self,
        mock_client: MagicMock,
        mock_get_list_items: MagicMock,
        mock_get_access_token: MagicMock,
        mock_get_nsb_2019_list_items: List[Dict[str, Any]],
    ):
        """Tests get_nsb_2019_list method"""
        mock_get_access_token.return_value = "abc"
        mock_get_list_items.return_value = mock_get_nsb_2019_list_items
        list_items = await get_nsb_2019_list(
            settings=Settings(), subject_id="656374"
        )
        mock_client.assert_called_once()
        assert 1 == len(list_items)

    @patch("aind_sharepoint_service_server.route.get_nsb_2019_list")
    async def test_get_nsb_2019(
        self,
        mock_get_nsb_2019_list: MagicMock,
        client: TestClient,
        mock_get_nsb_2019_list_items: List[Dict[str, Any]],
    ):
        """Tests get_nsb_2023 route"""
        mock_get_nsb_2019_list.return_value = mock_get_nsb_2019_list_items
        response = client.get("/nsb_2019/656374")
        assert 200 == response.status_code
        assert 1 == len(response.json())

    @patch("aind_sharepoint_service_server.route.get_access_token")
    @patch(
        "aind_sharepoint_service_server.handler.SessionHandler.get_list_items"
    )
    @patch("aind_sharepoint_service_server.route.AsyncClient")
    async def test_get_nsb_present_list(
        self,
        mock_client: MagicMock,
        mock_get_list_items: MagicMock,
        mock_get_access_token: MagicMock,
        mock_get_nsb_present_list_items: List[Dict[str, Any]],
    ):
        """Tests get_nsb_present_list method"""
        mock_get_access_token.return_value = "abc"
        mock_get_list_items.return_value = mock_get_nsb_present_list_items
        list_items = await get_nsb_present_list(
            settings=Settings(), subject_id="790025"
        )
        mock_client.assert_called_once()
        assert 1 == len(list_items)

    @patch("aind_sharepoint_service_server.route.get_nsb_present_list")
    async def test_get_nsb_present(
        self,
        mock_get_nsb_present_list: MagicMock,
        client: TestClient,
        mock_get_nsb_present_list_items: List[Dict[str, Any]],
    ):
        """Tests get_nsb_present route"""
        mock_get_nsb_present_list.return_value = (
            mock_get_nsb_present_list_items
        )
        response = client.get("/nsb_present/790025")
        assert 200 == response.status_code
        assert 1 == len(response.json())


if __name__ == "__main__":
    pytest.main([__file__])
