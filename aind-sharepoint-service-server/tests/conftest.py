"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Generator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from aind_sharepoint_service_server.main import app

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"


def mock_fetch_all_items(mocker: MockFixture, path: Path) -> MagicMock:
    """
    Patch SharePointClient._fetch_all_list_items to return records
    from resource files.
    """

    def fetch_side_effect(site_id, list_id, subject_id):
        """Side effect function to return items from JSONs"""
        all_items = []
        for file in sorted(path.glob("list_item*.json")):
            with open(file, encoding="utf-8") as f:
                records = json.load(f)
                items = [{"fields": records}]
                filtered = [
                    item
                    for item in items
                    if subject_id in item["fields"].get("Title")
                ]
                all_items.extend(filtered)
        return all_items

    mock_get = mocker.patch(
        "aind_sharepoint_service_server.client.SharePointClient."
        "_fetch_all_list_items"
    )
    mock_get.side_effect = fetch_side_effect
    return mock_get


@pytest.fixture()
def mock_las2020(mocker: MockFixture) -> MagicMock:
    """Expected las 2020 procedures."""
    return mock_fetch_all_items(mocker, path=RESOURCES_DIR / "las2020")


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    with TestClient(app) as c:
        yield c
