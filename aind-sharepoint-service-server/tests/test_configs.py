"""Tests configs module"""

import os
import unittest
from unittest.mock import patch
from pydantic import HttpUrl
from aind_sharepoint_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "SHAREPOINT_NSB_SITE_ID": "nsb_site_123",
            "SHAREPOINT_LAS_SITE_ID": "las_site_456",
            "SHAREPOINT_NSB_PRESENT_LIST_ID": "nsb_present",
            "SHAREPOINT_NSB_2019_LIST_ID": "nsb_2019",
            "SHAREPOINT_NSB_2023_LIST_ID": "nsb_2023",
            "SHAREPOINT_LAS_2020_LIST_ID": "las_2020",
            "SHAREPOINT_CLIENT_ID": "client_id",
            "SHAREPOINT_CLIENT_SECRET": "client_secret",
            "SHAREPOINT_TENANT_ID": "tenant_id",
        },
        clear=True,
    )
    def test_properties(self):
        """Tests resource_id property is set correctly"""
        settings = Settings()
        expected_settings = Settings(
            nsb_site_id="nsb_site_123",
            las_site_id="las_site_456",
            nsb_2023_list_id="nsb_2023",
            nsb_2019_list_id="nsb_2019",
            nsb_present_list_id="nsb_present",
            las_2020_list_id="las_2020",
            client_id="client_id",
            client_secret="client_secret",
            tenant_id="tenant_id",
        )
        expected_resource_id = "https://graph.microsoft.com/.default"
        expected_las_2020_url = HttpUrl(
            "https://graph.microsoft.com/v1.0"
            "/sites/las_site_456/lists/las_2020/items"
        )
        expected_nsb_2023_url = HttpUrl(
            "https://graph.microsoft.com/v1.0"
            "/sites/nsb_site_123/lists/nsb_2023/items"
        )
        expected_nsb_2019_url = HttpUrl(
            "https://graph.microsoft.com/v1.0"
            "/sites/nsb_site_123/lists/nsb_2019/items"
        )
        expected_nsb_present_url = HttpUrl(
            "https://graph.microsoft.com/v1.0"
            "/sites/nsb_site_123/lists/nsb_present/items"
        )
        self.assertEqual(expected_settings, settings)
        self.assertEqual(expected_resource_id, settings.resource_id)
        self.assertEqual(expected_las_2020_url, settings.las_2020_url)
        self.assertEqual(expected_nsb_2023_url, settings.nsb_2023_url)
        self.assertEqual(expected_nsb_2019_url, settings.nsb_2019_url)
        self.assertEqual(expected_nsb_present_url, settings.nsb_present_url)


if __name__ == "__main__":
    unittest.main()
