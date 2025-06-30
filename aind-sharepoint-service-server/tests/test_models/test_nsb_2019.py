"""Tests methods in NSB 2019 models module"""

import json
import os
from pathlib import Path
import unittest
from aind_sharepoint_service_server.models.nsb_2019 import NSB2019List

RESOURCES_DIR = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".." / "resources"
)


class TestNSB2019List(unittest.TestCase):
    """Tests methods in NSB2019List class"""

    @classmethod
    def setUpClass(cls):
        """Load json files before running tests."""
        with open(RESOURCES_DIR / "nsb_2019_first_response.json") as f:
            nsb_2019_list = json.load(f)

        cls.nsb_2019_list = nsb_2019_list["value"]

    def test_models_parsed(self):
        """Tests that the given list item files are parsed without error."""
        models = [
            NSB2019List.model_validate(list_item)
            for list_item in self.nsb_2019_list
        ]
        self.assertIsNotNone(models)


if __name__ == "__main__":
    unittest.main()
