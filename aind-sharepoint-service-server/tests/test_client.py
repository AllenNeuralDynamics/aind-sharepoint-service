"""Module to test SharePoint Client methods"""

import json
import logging
import os
import unittest
from pathlib import Path
from typing import List, Tuple
from unittest.mock import MagicMock, call, patch

import requests
from fastapi.responses import JSONResponse
from pydantic import SecretStr

from aind_sharepoint_service_server.client import SharePointClient
from aind_sharepoint_service_server.configs import Settings


from tests import PYD_VERSION


class TestSharepointClient(unittest.TestCase):
    """Class to test methods for SharePointClient."""

    @classmethod
    def setUpClass(cls):
        """Load json files before running tests."""
        cls.settings = Settings(
            aind_site_id="aind_site_123",
            las_site_id="las_site_456",
            nsb_2019_list_id="nsb_2019",
            nsb_2023_list_id="nsb_2023",
            nsb_present_list_id="nsb_present",
            las_2020_list_id="las_2020",
            client_id="client_id",
            client_secret=SecretStr("client_secret"),
            tenant_id="tenant_id",
            graph_api_url="https://graph.microsoft.com/v1.0",
            scope="https://graph.microsoft.com/.default",
            token_url="some_url",
        )
        cls.client = SharePointClient.from_settings(cls.settings)
        cls.client.get_access_token = MagicMock(return_value="fake-token")
        
    def test_get_access_token_success(self):
        """Test that get_access_token returns and caches the access token."""

        client = SharePointClient.from_settings(self.settings)
        # Ensure no token is cached initially.
        client._access_token = None
        fake_token = "abc123"
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {"access_token": fake_token}

        with patch("requests.post", return_value=fake_response) as mock_post:
            token = client.get_access_token()
            self.assertEqual(token, fake_token)
            token2 = client.get_access_token()
            self.assertEqual(token2, fake_token)
            self.assertEqual(mock_post.call_count, 1)

    def test_get_access_token_failure(self):
        """Test that get_access_token raises RuntimeError when
        the GET request fails."""
        client = SharePointClient.from_settings(self.settings)
        client._access_token = None
        with patch("requests.get") as mock_get:
            fake_response = MagicMock()
            fake_response.raise_for_status.side_effect = (
                requests.exceptions.RequestException("Error")
            )
            mock_get.return_value = fake_response
            with self.assertRaises(RuntimeError) as context:
                client.get_access_token()
            self.assertIn(
                "Failed to authenticate with SharePoint",
                str(context.exception),
            )

    def test_get_headers(self):
        """Test that _get_headers constructs the correct headers
        using the access token."""
        client = SharePointClient.from_settings(self.settings)
        client.get_access_token = MagicMock(return_value="mytoken")
        headers = client._get_headers()
        expected_headers = {
            "Authorization": "Bearer mytoken",
            "Content-Type": "application/json",
        }
        self.assertEqual(headers, expected_headers)

    def test_fetch_list_items_success(self):
        """Test that JSON is returned from successful GET call."""
        client = SharePointClient.from_settings(self.settings)
        # Patch _get_headers to return a fixed header.
        client._get_headers = MagicMock(
            return_value={
                "Authorization": "Bearer fake",
                "Content-Type": "application/json",
            }
        )
        fake_json = {"value": [{"fields": {"some": "data"}}]}
        fake_response = MagicMock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = fake_json

        with patch("requests.get", return_value=fake_response) as mock_get:
            site_id = "aind_site_123"
            list_id = "nsb_2019"
            subject_id = "12345"
            subject_alias = "lab_tracks_id"
            result = client._fetch_list_items(
                site_id, list_id, subject_id, subject_alias
            )
            self.assertEqual(result, fake_json)
            expected_url = (
                f"{client.graph_api_url}/sites/{site_id}/lists/{list_id}/items"
            )
            expected_params = {
                "expand": "fields",
                "$filter": f"fields/{subject_alias} eq '{subject_id}'",
            }
            mock_get.assert_called_once_with(
                expected_url,
                headers={
                    "Authorization": "Bearer fake",
                    "Content-Type": "application/json",
                },
                params=expected_params,
            )

    def test_fetch_list_items_failure(self):
        """Test that _fetch_list_items raises error when GET call fails."""
        client = SharePointClient.from_settings(self.settings)
        client._get_headers = MagicMock(
            return_value={
                "Authorization": "Bearer fake",
                "Content-Type": "application/json",
            }
        )
        with patch(
            "requests.get",
            side_effect=requests.exceptions.RequestException("Error"),
        ):
            site_id = "aind_site_123"
            list_id = "nsb_2019"
            subject_id = "12345"
            subject_alias = "lab_tracks_id"
            with self.assertRaises(RuntimeError) as context:
                client._fetch_list_items(
                    site_id, list_id, subject_id, subject_alias
                )
            self.assertIn(
                f"Failed to fetch list items for list {list_id}.",
                str(context.exception),
            )

    def test_fetch_all_list_items_success(self):
        """Test that list is returned from successful GET call."""

        client = SharePointClient.from_settings(self.settings)
        client._get_headers = MagicMock(
            return_value={
                "Authorization": "Bearer fake",
                "Content-Type": "application/json",
            }
        )
        fake_paginated_items = [
            {"fields": {"Title": "000000 000001", "some": "data"}},
            {"fields": {"Title": "111111", "some": "data2"}},
            {"fields": {"Title": "000000 000002", "some": "data3"}},
        ]
        with patch.object(
            client, "_paginate", return_value=iter(fake_paginated_items)
        ) as mock_paginate:
            site_id = "aind_site_123"
            list_id = "las_2020"
            subject_id = "000000"

            result = client._fetch_all_list_items(
                site_id=site_id, list_id=list_id, subject_id=subject_id
            )
            expected_result = [
                {"fields": {"Title": "000000 000001", "some": "data"}},
                {"fields": {"Title": "000000 000002", "some": "data3"}},
            ]
            self.assertEqual(result, expected_result)

            expected_url = (
                f"{client.graph_api_url}/sites/{site_id}/lists/{list_id}/items"
            )
            expected_params = {
                "expand": "fields",
                "$filter": "fields/ReqPro1 eq 'Retro-Orbital Injection'",
            }
            mock_paginate.assert_called_once()
            called_kwargs = mock_paginate.call_args.kwargs
            self.assertEqual(called_kwargs.get("url"), expected_url)
            self.assertEqual(called_kwargs.get("params"), expected_params)
            self.assertIn("session", called_kwargs)

    def test_paginate(self):
        """Tests that _paginate properly iterates through paginated data."""

        client = SharePointClient.from_settings(self.settings)
        initial_url = (
            f"{client.graph_api_url}/sites/aind_site_123/lists/las_2020/items"
        )
        initial_params = {
            "expand": "fields",
            "$filter": "fields/ReqPro1 eq 'Retro-Orbital Injection'",
        }
        fake_response1 = MagicMock()
        fake_response1.raise_for_status.return_value = None
        fake_response1.json.return_value = {
            "value": [{"id": 1}, {"id": 2}],
            "@odata.nextLink": f"{initial_url}?page=2",
        }
        # response from the second page
        fake_response2 = MagicMock()
        fake_response2.raise_for_status.return_value = None
        fake_response2.json.return_value = {
            "value": [{"id": 3}],
        }
        fake_session = MagicMock()
        fake_session.get.side_effect = [fake_response1, fake_response2]
        results = list(
            SharePointClient._paginate(
                initial_url, initial_params, fake_session
            )
        )
        expected_results = [{"id": 1}, {"id": 2}, {"id": 3}]
        self.assertEqual(results, expected_results)
        expected_calls = [
            call(initial_url, params=initial_params),
            call(f"{initial_url}?page=2", params=None),
        ]
        fake_session.get.assert_has_calls(expected_calls)


if __name__ == "__main__":
    unittest.main()