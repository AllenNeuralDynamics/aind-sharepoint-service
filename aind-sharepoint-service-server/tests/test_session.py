"""Tests session module"""

import pytest

from aind_sharepoint_service_server.session import get_session


class TestSession:
    """Test methods in Session Class"""

    def test_get_session(self):
        """Tests get_session method"""

        session = next(get_session())
        assert "aind_site_id" == session.aind_site_id
        assert "las_site_id" == session.las_site_id
        assert "https://graph.microsoft.com/v1.0" == session.graph_api_url


if __name__ == "__main__":
    pytest.main([__file__])
