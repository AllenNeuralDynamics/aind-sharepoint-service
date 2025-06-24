"""Module to handle requesting info from Sharepoint"""

from typing import Any, Dict, List

from httpx import AsyncClient


class SessionHandler:
    """Handle pulling data from Sharepoint lists"""

    def __init__(self, client: AsyncClient):
        """
        Class constructor.
        Parameters
        ----------
        client : AsyncClient
        """
        self.client = client

    async def get_list_items(
        self, list_items_url: str, params: Dict[str, str]
    ) -> List[Dict[str, Any]]:
        """
        Paginate through a list to return all items filtered by params.
        Parameters
        ----------
        list_items_url : str
        params : Dict[str, str]

        Returns
        -------
        List[Dict[str, Any]]

        """
        all_items = []
        response = await self.client.get(list_items_url, params=params)
        response.raise_for_status()
        for result in response.json().get("value", []):
            all_items.append(result)
        next_link = response.json().get("@odata.nextLink")
        while next_link:
            response = await self.client.get(next_link)
            response.raise_for_status()
            for result in response.json().get("value", []):
                all_items.append(result)
            next_link = response.json().get("@odata.nextLink")
        return all_items
