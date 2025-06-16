"""Module to create client to connect to sharepoint database"""

import logging
from typing import Any, Iterator, Optional

import requests
from pydantic import SecretStr, ValidationError, ValidatorFunctionWrapHandler
from requests import Session

from aind_sharepoint_service_server.configs import Settings


def optional_enum(
    v: Any, handler: ValidatorFunctionWrapHandler
) -> Optional[Any]:
    """
    Utility for parsing sharepoint model.
    If an enum value does not exist, will use None instead
    Parameters
    ----------
    v : Any
        The value to validate.
    handler : ValidatorFunctionWrapHandler
        The handler for the validation function.
    Returns
    -------
    Optional[Any]
        The validated value or None if validation fails.
    """
    try:
        validated_v = handler(v)
        return validated_v
    except ValidationError:
        return None


class SharePointClient:
    """This class contains the API to connect to Sharepoint Database."""

    def __init__(
        self,
        aind_site_id: str,
        las_site_id: str,
        nsb_2019_list_id: str,
        nsb_2023_list_id: str,
        nsb_present_list_id: str,
        las_2020_list_id: str,
        client_id: str,
        client_secret: SecretStr,
        tenant_id: str,
        graph_api_url: str,
        scope: str,
        token_url: str,
    ) -> None:
        """
        Initailize the SharePointClient with the required parameters.
        Parameters
        ----------
        aind_site_id : str
            Sharepoint Site ID for AIND Domain
        las_site_id : str
            Sharepoint Site ID for LAS Domain
        nsb_2019_list_id : str
            List ID for NSB 2019-2022 procedures
        nsb_2023_list_id : str
            List ID for NSB 2023-2024 Archive procedures
        nsb_present_list_id : str
            List ID for NSB 2023-Present procedures
        las_2020_list_id : str
            List ID for LAS 2020 procedures
        client_id : str
            Client ID for the principal account
        client_secret : SecretStr
            Client Secret for the principal account
        tenant_id : str
            Tenant ID for the principal account
        graph_api_url : str
            URL for the Microsoft Graph API
        scope : str
            Scope for the Microsoft Graph API
        token_url : str
            URL for the Microsoft Identity
        """
        self.aind_site_id = aind_site_id
        self.las_site_id = las_site_id
        self.nsb_2019_list_id = nsb_2019_list_id
        self.nsb_2023_list_id = nsb_2023_list_id
        self.nsb_present_list_id = nsb_present_list_id
        self.las_2020_list_id = las_2020_list_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.token_url = token_url
        self.graph_api_url = graph_api_url
        self.scope = scope
        self._access_token: Optional[str] = None

    @classmethod
    def from_settings(cls, settings: Settings):
        """
        Create a SharePointClient instance from a Settings object.
        """
        return cls(
            aind_site_id=settings.aind_site_id,
            las_site_id=settings.las_site_id,
            nsb_2019_list_id=settings.nsb_2019_list_id,
            nsb_2023_list_id=settings.nsb_2023_list_id,
            nsb_present_list_id=settings.nsb_present_list_id,
            las_2020_list_id=settings.las_2020_list_id,
            client_id=settings.client_id,
            client_secret=settings.client_secret,
            tenant_id=settings.tenant_id,
            graph_api_url=settings.graph_api_url,
            scope=settings.scope,
            token_url=settings.token_url,
        )

    def get_access_token(self) -> str:
        """Obtain an OAuth access token from Microsoft Identity Platform."""
        if self._access_token:
            return self._access_token
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret.get_secret_value(),
            "scope": self.scope,
        }
        try:
            response = requests.post(self.token_url, data=payload)
            response.raise_for_status()
            self._access_token = response.json().get("access_token")
            return self._access_token
        except requests.exceptions.RequestException as e:
            logging.error(f"Error obtaining access token: {e}")
            raise RuntimeError("Failed to authenticate with SharePoint.")

    def _get_headers(self) -> dict:
        """Construct the request headers using the access token."""
        token = self.get_access_token()
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _paginate(url: str, params: dict, session: Session) -> Iterator[dict]:
        """

        Parameters
        ----------
        url : str
        params : dict
        session : Session

        Returns
        -------
        Iterator[dict]

        """
        while True:
            response = session.get(url, params=params)
            response.raise_for_status()
            for result in response.json().get("value", []):
                yield result

            if not response.json().get("@odata.nextLink"):
                return

            url = response.json().get("@odata.nextLink")
            params = None

    def _fetch_all_list_items(
        self, site_id: str, list_id: str, subject_id: str
    ) -> list:
        """
        Fetch all items from a LAS SharePoint list using the Graph API.
        Implements pagination for large lists correctly. Filters by
        Retro-Orbital Injections.
        """
        url = f"{self.graph_api_url}/sites/{site_id}/lists/{list_id}/items"
        params = {
            "expand": "fields",
            "$filter": "fields/ReqPro1 eq 'Retro-Orbital Injection'",
        }
        headers = self._get_headers()
        all_items = []
        with Session() as session:
            session.headers.update(headers)
            paginator = self._paginate(url=url, params=params, session=session)
            for item in paginator:
                if subject_id in item.get("fields", dict()).get("Title", ""):
                    all_items.append(item)
        return all_items

    def _fetch_list_items(
        self, site_id: str, list_id: str, subject_id: str, subject_alias: str
    ) -> dict:
        """
        Fetch items from a SharePoint list using the Graph API.
        Handles simple filtering by subject_id.
        """
        params = {
            "expand": "fields",
            "$filter": f"fields/{subject_alias} eq '{subject_id}'",
        }
        try:
            response = requests.get(
                f"{self.graph_api_url}/sites/{site_id}/lists/{list_id}/items",
                headers=self._get_headers(),
                params=params,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(
                f"Error fetching list items from list {list_id}: {e}"
            )
            raise RuntimeError(
                f"Failed to fetch list items for list {list_id}."
            )
