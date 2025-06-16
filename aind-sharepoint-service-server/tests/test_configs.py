"""Tests configs module"""

import os
import unittest
from unittest.mock import patch

from aind_sharepoint_service_server.configs import Settings
from tests import PYD_VERSION


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "SHAREPOINT_AIND_SITE_ID": "aind_site_123",
            "SHAREPOINT_LAS_SITE_ID": "las_site_456",
            "SHAREPOINT_NSB_2019_LIST_ID": "nsb_2019",
            "SHAREPOINT_NSB_2023_LIST_ID": "nsb_2023",
            "SHAREPOINT_NSB_PRESENT_LIST_ID": "nsb_present",
            "SHAREPOINT_LAS_2020_LIST_ID": "las_2020",
            "SHAREPOINT_CLIENT_ID": "client_id",
            "SHAREPOINT_CLIENT_SECRET": "client_secret",
            "SHAREPOINT_TENANT_ID": "tenant_id",
        },
        clear=True,
    )
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings()
        expected_settings = Settings(
            aind_site_id="aind_site_123",
            las_site_id="las_site_456",
            nsb_2019_list_id="nsb_2019",
            nsb_2023_list_id="nsb_2023",
            nsb_present_list_id="nsb_present",
            las_2020_list_id="las_2020",
            client_id="client_id",
            client_secret="client_secret",
            tenant_id="tenant_id",
            graph_api_url="https://graph.microsoft.com/v1.0",
            scope="https://graph.microsoft.com/.default",
            token_url=(
                "https://login.microsoftonline.com/tenant_id/oauth2/v2.0/token"
            ),
        )
        self.assertEqual(expected_settings, settings)

    @patch.dict(os.environ, {}, clear=True)
    def test_settings_errors(self):
        """Tests that errors are raised if settings are incorrect."""

        with self.assertRaises(ValueError) as e:
            Settings(aind_site_id="aind_site_only")

        expected_error_message = (
            "9 validation errors for Settings\n"
            "las_site_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "nsb_2019_list_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "nsb_2023_list_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "nsb_present_list_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "las_2020_list_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "client_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "client_secret\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "tenant_id\n"
            "  Field required [type=missing, input_value={'aind_site_id': "
            "'aind_site_only'}, input_type=dict]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/missing\n"
            "token_url\n"
            "  Value error, tenant_id must be provided to generate token_url "
            "[type=value_error, input_value=None, input_type=NoneType]\n"
            "    For further information visit "
            f"https://errors.pydantic.dev/{PYD_VERSION}/v/value_error"
        )

        self.assertEqual(expected_error_message, repr(e.exception))


if __name__ == "__main__":
    unittest.main()
