"""Set up fixtures to be used across all test modules."""

import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from requests import Response
from typing import Any, Generator
from aind_sharepoint_service_server.main import app
import json
from unittest.mock import MagicMock
from pytest_mock import MockFixture

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

def mock_fetch_all_items(mocker: MockFixture, path: Path) -> MagicMock:
    """
    Patch SharePointClient._fetch_all_list_items to return records from resource files.
    """
    def fetch_side_effect(site_id, list_id, subject_id):
        all_items = []
        for file in sorted(path.glob("list_item*.json")):
            with open(file, encoding="utf-8") as f:
                records = json.load(f)
                all_items.append(records)
        return all_items

    mock_get = mocker.patch("aind_sharepoint_service_server.client.SharePointClient._fetch_all_list_items")
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
