"""Tests methods in models module"""

import json
import logging
import os
import unittest
from pathlib import Path

from aind_sharepoint_service_server.models import (
    HealthCheck,
    LASList,
    LASProtocol,
)

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


class TestHealthCheck(unittest.TestCase):
    """Tests for HealthCheck class"""

    def test_constructor(self):
        """Basic test for class constructor"""

        health_check = HealthCheck()
        self.assertEqual("OK", health_check.status)


class TestLASList(unittest.TestCase):
    """Tests methods in LASList class"""

    @classmethod
    def setUpClass(cls):
        """Load json files before running tests."""
        cls.list_items = []
        cls.file_names = []
        las_dir = RESOURCES_DIR / "las2020"
        for file in sorted(las_dir.glob("list_item*.json")):
            with open(file, encoding="utf-8") as f:
                contents = json.load(f)
                cls.list_items.append(contents)
                cls.file_names.append(file.name)

    def test_models_parsed(self):
        """Tests that the given list item files are parsed without error."""
        for index, list_item in enumerate(self.list_items):
            logging.debug(f"Processing file: {self.file_names[index]}")
            las_model = LASList.model_validate(list_item)
            self.assertEqual(
                las_model.author_id, int(list_item.get("AuthorId"))
            )

    def test_optional_enum_meta_case(self):
        """Tests optional enum wrapper returns None as expected."""
        list_item = self.list_items[0]
        las_model = LASList.model_validate(list_item)
        self.assertEqual(
            LASProtocol.N_2212_INVESTIGATING_BRAI, las_model.protocol
        )
        self.assertIsNone(las_model.bc_type)


if __name__ == "__main__":
    unittest.main()
