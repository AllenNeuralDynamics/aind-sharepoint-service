"""Module to test main app"""

import pytest
from fastapi.routing import APIRoute
from fastapi.testclient import TestClient
from aind_sharepoint_service_server.route import router


class TestMain:
    """Tests app endpoints"""

    def test_app_with_in_memory_cache(self, client: TestClient):
        """Tests client is instantiated correctly when redis_url None."""
        response = client.get("/healthcheck")
        assert 200 == response.status_code

    def test_app_with_redis(self, client_with_redis: TestClient):
        """Tests client is instantiated correctly when redis_url set."""
        response = client_with_redis.get("/healthcheck")
        assert 200 == response.status_code

    def test_operation_ids_are_set(self, client: TestClient):
        """Test that operation_id is set to route name for all APIRoutes."""
        api_routes = [r for r in router.routes if isinstance(r, APIRoute)]
        assert len(api_routes) > 0
        assert all(r.operation_id == r.name for r in api_routes)


if __name__ == "__main__":
    pytest.main([__file__])
