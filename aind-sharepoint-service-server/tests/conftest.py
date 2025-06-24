"""Set up fixtures to be used across all test modules."""

import json
import os
from pathlib import Path
from typing import Any, Dict, Generator, List
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from aind_sharepoint_service_server.configs import Settings

RESOURCES_DIR = Path(os.path.dirname(os.path.realpath(__file__))) / "resources"

patch(
    "fastapi_cache.decorator.cache", lambda *args, **kwargs: lambda f: f
).start()


@pytest.fixture(scope="session")
def mock_get_las_2020_responses() -> AsyncMock:
    """Mock responses fetching LAS 2020 list"""
    with open(RESOURCES_DIR / "las_2020_first_response.json", "r") as f:
        first_response = json.load(f)
    with open(RESOURCES_DIR / "las_2020_second_response.json", "r") as f:
        second_response = json.load(f)
    mock_client = AsyncMock()
    mock_first_response = MagicMock(status_code=200)
    mock_first_response.raise_for_status.return_value = None
    mock_first_response.json.return_value = first_response
    mock_second_response = MagicMock(status_code=200)
    mock_second_response.raise_for_status.return_value = None
    mock_second_response.json.return_value = second_response
    mock_client.get.side_effect = [mock_first_response, mock_second_response]
    return mock_client


@pytest.fixture(scope="session")
def mock_get_las_2020_list_items() -> List[Dict[str, Any]]:
    """Mock LAS 2020 list items"""
    with open(RESOURCES_DIR / "las_2020_first_response.json", "r") as f:
        first_response = json.load(f)
    with open(RESOURCES_DIR / "las_2020_second_response.json", "r") as f:
        second_response = json.load(f)
    all_items = first_response["value"]
    all_items.extend(second_response["value"])
    return all_items


@pytest.fixture(scope="session")
def mock_get_nsb_2023_list_items() -> List[Dict[str, Any]]:
    """Mock NSB 2023 list items"""
    with open(RESOURCES_DIR / "nsb_2023_first_response.json", "r") as f:
        first_response = json.load(f)
    all_items = first_response["value"]
    return all_items


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, Any, None]:
    """Creating a client for testing purposes."""

    # Import moved to be able to mock cache
    from aind_sharepoint_service_server.main import app

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def client_with_redis() -> Generator[TestClient, Any, None]:
    """Creating a client when settings have a redis_url. Only used in one test
    to verify the lifespan method in main is called correctly."""

    # Import moved to be able to mock cache
    from aind_sharepoint_service_server.main import app

    settings = Settings()
    settings_with_redis = settings.model_copy(
        update={"redis_url": "redis"}, deep=True
    )
    with (
        patch(
            "aind_sharepoint_service_server.main.get_settings",
            return_value=settings_with_redis,
        ),
        patch(
            "aind_sharepoint_service_server.main.from_url", return_value=None
        ),
        patch(
            "aind_sharepoint_service_server.main.RedisBackend",
            return_value=None,
        ),
    ):
        with TestClient(app) as c:
            yield c
