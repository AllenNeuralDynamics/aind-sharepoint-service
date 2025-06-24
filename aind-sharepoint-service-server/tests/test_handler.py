"""Tests for handler module"""

import pytest

from aind_sharepoint_service_server.handler import SessionHandler


@pytest.mark.asyncio
class TestSessionHandler:
    """Tests methods in SessionHandler class"""

    async def test_get_list_items(self, mock_get_las_2020_responses):
        """Tests get_list_items method."""
        session_handler = SessionHandler(client=mock_get_las_2020_responses)
        result = await session_handler.get_list_items(
            list_items_url="", params=dict()
        )
        print(mock_get_las_2020_responses.get.mock_calls)
        assert len(result) == 4


if __name__ == "__main__":
    pytest.main([__file__])
