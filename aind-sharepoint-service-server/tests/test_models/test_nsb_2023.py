"""Tests methods in NSB 2023 models module"""

import json
import os
from pathlib import Path
import unittest
from aind_sharepoint_service_server.models.nsb_2023 import NSB2023List

RESOURCES_DIR = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".." / "resources"
)


class TestNSB2023List(unittest.TestCase):
    """Tests methods in NSB2023List class"""

    @classmethod
    def setUpClass(cls):
        """Load json files before running tests."""
        with open(RESOURCES_DIR / "nsb_2023_first_response.json") as f:
            nsb_2023_list = json.load(f)

        cls.nsb_2023_list = nsb_2023_list["value"]

    def test_models_parsed(self):
        """Tests that the given list item files are parsed without error."""
        models = [
            NSB2023List.model_validate(list_item)
            for list_item in self.nsb_2023_list
        ]
        self.assertIsNotNone(models)


if __name__ == "__main__":
    unittest.main()
