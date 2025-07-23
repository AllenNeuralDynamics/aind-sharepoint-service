"""Module for settings to connect to backend"""

from typing import ClassVar, Optional
from urllib.parse import urljoin

from aind_settings_utils.aws import SecretsManagerBaseSettings
from pydantic import Field, RedisDsn, SecretStr
from pydantic_settings import SettingsConfigDict


class Settings(SecretsManagerBaseSettings):
    """Settings needed to connect to Sharepoint database"""

    model_config = SettingsConfigDict(
        env_prefix="SHAREPOINT_", case_sensitive=False
    )
    las_site_id: str = Field(
        title="Site ID",
        description="Site ID of the SharePoint site.",
    )
    nsb_site_id: str = Field(
        title="Site ID",
        description="Site ID of the SharePoint site.",
    )
    nsb_2019_list_id: str = Field(
        title="NSB 2019-2022 List ID",
        description="List ID for NSB 2019-2022 Sharepoint List.",
    )
    nsb_2023_list_id: str = Field(
        title="NSB 2023-Archive List ID",
        description="List ID for NSB 2023-Archive Sharepoint List.",
    )
    nsb_present_list_id: str = Field(
        title="NSB 2023-Present List ID",
        description="List ID for NSB 2023-Present Sharepoint List.",
    )
    las_2020_list_id: str = Field(
        title="LAS 2020 List ID",
        description="List ID for LAS 2020 Sharepoint List.",
    )
    client_id: str = Field(
        title="Client ID",
        description="Client ID for the principal account.",
    )
    client_secret: SecretStr = Field(
        title="Client Secret",
        description="Client Secret for the principal account.",
    )
    tenant_id: str = Field(
        title="Tenant ID",
        description="Tenant ID for the principal account.",
    )
    redis_url: Optional[RedisDsn] = Field(default=None)
    graph_api_url: ClassVar[str] = "https://graph.microsoft.com"

    @property
    def resource_id(self) -> str:
        """Resource id used in Credentials scope."""
        return urljoin(self.graph_api_url, ".default")

    @property
    def las_2020_url(self) -> str:
        """LAS 2020 list items url"""
        return urljoin(
            self.graph_api_url,
            (
                f"v1.0/sites/{self.las_site_id}"
                f"/lists/{self.las_2020_list_id}/items"
            ),
        )

    @property
    def nsb_2019_url(self) -> str:
        """NSB 2019-2022 list items url"""
        return urljoin(
            self.graph_api_url,
            (
                f"v1.0/sites/{self.nsb_site_id}"
                f"/lists/{self.nsb_2019_list_id}/items"
            ),
        )

    @property
    def nsb_2023_url(self) -> str:
        """NSB 2023 list items url"""
        return urljoin(
            self.graph_api_url,
            (
                f"v1.0/sites/{self.nsb_site_id}"
                f"/lists/{self.nsb_2023_list_id}/items"
            ),
        )

    @property
    def nsb_present_url(self) -> str:
        """NSB Present list items url"""
        return urljoin(
            self.graph_api_url,
            (
                f"v1.0/sites/{self.nsb_site_id}"
                f"/lists/{self.nsb_present_list_id}/items"
            ),
        )


settings = Settings()
