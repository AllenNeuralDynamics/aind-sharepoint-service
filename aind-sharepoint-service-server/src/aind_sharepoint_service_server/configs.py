"""Module for settings to connect to backend"""

from typing import Optional

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, SecretStr, field_validator
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Settings needed to connect to Sharepoint database"""

    model_config = SettingsConfigDict(
        env_prefix="SHAREPOINT_", case_sensitive=False
    )

    aind_site_id: str = Field(
        title="AIND Site ID",
        description="Site ID of the AIND SharePoint site.",
    )
    las_site_id: str = Field(
        title="LAS Site ID",
        description="Site ID of the LAS SharePoint site.",
    )
    nsb_2019_list_id: str = Field(
        title="NSB 2019-2022 Archive List ID",
        description="List ID for NSB 2019-2022 procedures.",
    )
    nsb_2023_list_id: str = Field(
        title="NSB 2023-2024 Archive List ID",
        description="List ID for NSB 2023-2024 Archive procedures.",
    )
    nsb_present_list_id: str = Field(
        title="NSB 2023-Present List ID",
        description="List ID for NSB Present procedures.",
    )
    las_2020_list_id: str = Field(
        title="LAS 2020 List ID",
        description="List ID for LAS 2020 procedures.",
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
    graph_api_url: str = Field(
        title="Graph API URL",
        description="URL for the Microsoft Graph API.",
        default="https://graph.microsoft.com/v1.0",
    )
    scope: str = Field(
        title="Scope",
        description="Scope for the Microsoft Graph API.",
        default="https://graph.microsoft.com/.default",
    )
    token_url: Optional[str] = Field(
        None,
        title="Token URL",
        description="URL for the Microsoft Identity Platform.",
    )

    @field_validator("token_url", mode="before")
    def set_token_url(cls, v, info):
        """Sets token_url from tenant_id if not provided."""
        if v is not None:
            return v
        tenant_id = info.data.get("tenant_id")
        if not tenant_id:
            raise ValueError(
                "tenant_id must be provided to generate token_url"
            )
        return (
            f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        )
