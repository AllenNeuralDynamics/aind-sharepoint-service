"""Tests methods in LAS 2020 models module"""

import json
import os
import unittest
from pathlib import Path

from aind_sharepoint_service_server.models.las_2020 import Las2020List

RESOURCES_DIR = (
    Path(os.path.dirname(os.path.realpath(__file__))) / ".." / "resources"
)


class TestLAS2020List(unittest.TestCase):
    """Tests methods in LAS2020List class"""

    @classmethod
    def setUpClass(cls):
        """Load json files before running tests."""
        with open(RESOURCES_DIR / "las_2020_second_response.json") as f:
            las_2020_list = json.load(f)

        cls.las_2020_list = las_2020_list["value"]

    def test_models_parsed(self):
        """Tests that item jsons can be parsed into models without errors."""
        models = [
            Las2020List.model_validate(list_item)
            for list_item in self.las_2020_list
        ]
        self.assertIsNotNone(models)


if __name__ == "__main__":
    unittest.main()
