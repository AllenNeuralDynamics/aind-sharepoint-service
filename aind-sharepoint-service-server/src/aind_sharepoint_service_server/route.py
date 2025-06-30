"""Module to handle endpoint responses"""

from typing import Any, Dict, List

from azure.core.credentials import AccessToken
from azure.identity import ClientSecretCredential
from fastapi import APIRouter, Depends, Path, status
from fastapi_cache.decorator import cache
from httpx import AsyncClient

from aind_sharepoint_service_server.configs import Settings, get_settings
from aind_sharepoint_service_server.handler import SessionHandler
from aind_sharepoint_service_server.models.core import HealthCheck
from aind_sharepoint_service_server.models.las_2020 import Las2020List
from aind_sharepoint_service_server.models.nsb_2019 import NSB2019List
from aind_sharepoint_service_server.models.nsb_2023 import NSB2023List

router = APIRouter()


@cache(expire=3360)
async def get_access_token(settings: Settings) -> str:
    """
    Get access token from either Azure or cache. Token is valid for 60 minutes.
    We set cache lifespan to 56 minutes.

    Returns
    -------
    str

    """
    credentials: AccessToken = ClientSecretCredential(
        tenant_id=settings.tenant_id,
        client_id=settings.client_id,
        client_secret=settings.client_secret.get_secret_value(),
    ).get_token(settings.resource_id)
    return credentials.token


@cache(expire=3600)
async def get_las_2020_list(settings: Settings) -> List[Dict[str, Any]]:
    """Get the LAS_2020 list items"""
    bearer_token = await get_access_token(settings=settings)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    params = {
        "expand": "fields",
        "$filter": "fields/ReqPro1 eq 'Retro-Orbital Injection'",
    }
    async with AsyncClient(headers=headers) as client:
        session_handler = SessionHandler(client=client)
        list_items = await session_handler.get_list_items(
            list_items_url=settings.las_2020_url, params=params
        )
    return list_items


# Not worthwhile to cache results for NSB lists
async def get_nsb_2019_list(
    subject_id: str, settings: Settings
) -> List[Dict[str, Any]]:
    """Get the NSB_2019 list items"""
    bearer_token = await get_access_token(settings=settings)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    params = {
        "expand": "fields",
        "$filter": f"fields/LabTracks_x0020_ID eq '{subject_id}'",
    }
    async with AsyncClient(headers=headers) as client:
        session_handler = SessionHandler(client=client)
        list_items = await session_handler.get_list_items(
            list_items_url=settings.nsb_2019_url, params=params
        )
    return list_items


async def get_nsb_2023_list(
    subject_id: str, settings: Settings
) -> List[Dict[str, Any]]:
    """Get the NSB_2023 list items"""
    bearer_token = await get_access_token(settings=settings)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    params = {
        "expand": "fields",
        "$filter": f"fields/LabTracks_x0020_ID1 eq '{subject_id}'",
    }
    async with AsyncClient(headers=headers) as client:
        session_handler = SessionHandler(client=client)
        list_items = await session_handler.get_list_items(
            list_items_url=settings.nsb_2023_url, params=params
        )
    return list_items


async def get_nsb_present_list(
    subject_id: str, settings: Settings
) -> List[Dict[str, Any]]:
    """Get the NSB Present list items"""
    bearer_token = await get_access_token(settings=settings)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }
    params = {
        "expand": "fields",
        "$filter": f"fields/LabTracks_x0020_ID1 eq '{subject_id}'",
    }
    async with AsyncClient(headers=headers) as client:
        session_handler = SessionHandler(client=client)
        list_items = await session_handler.get_list_items(
            list_items_url=settings.nsb_present_url, params=params
        )
    return list_items


@router.get(
    "/healthcheck",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    """
    ## Endpoint to perform a healthcheck on.

    Returns:
        HealthCheck: JSON response with the health status
    """
    return HealthCheck()


@router.get(
    "/las_2020/{subject_id}",
    response_model=List[Las2020List],
)
async def get_las_2020(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for LAS 2020",
                "value": "805811",
            }
        },
    ),
    settings=Depends(get_settings),
):
    """
    # LAS 2020 Endpoint
    Retrieve information from the LAS 2020 list for a given subject ID.
    """
    las_2020_list = await get_las_2020_list(settings=settings)
    las_2020_models = [
        Las2020List.model_validate(item["fields"])
        for item in las_2020_list
        if subject_id in item.get("fields", dict()).get("Title", "").split(" ")
    ]
    return las_2020_models


@router.get(
    "/nsb_2019/{subject_id}",
    response_model=List[NSB2019List],
)
async def get_nsb_2019(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for NSB 2019",
                "value": "656374",
            }
        },
    ),
    settings=Depends(get_settings),
):
    """
    # NSB 2019 Endpoint
    Retrieve information from the NSB 2019 list for a given subject ID.
    """

    nsb_2019_list = await get_nsb_2019_list(
        subject_id=subject_id, settings=settings
    )
    nsb_2019_models = [
        NSB2019List.model_validate(item["fields"]) for item in nsb_2019_list
    ]
    return nsb_2019_models


@router.get(
    "/nsb_2023/{subject_id}",
    response_model=List[NSB2023List],
)
async def get_nsb_2023(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for NSB 2023",
                "value": "657849",
            }
        },
    ),
    settings=Depends(get_settings),
):
    """
    # NSB 2023 Endpoint
    Retrieve information from the NSB 2023-Archive list for a given subject ID.
    """

    nsb_2023_list = await get_nsb_2023_list(
        subject_id=subject_id, settings=settings
    )
    nsb_2023_models = [
        NSB2023List.model_validate(item["fields"]) for item in nsb_2023_list
    ]
    return nsb_2023_models


@router.get(
    "/nsb_present/{subject_id}",
    response_model=List[NSB2023List],
)
async def get_nsb_present(
    subject_id: str = Path(
        ...,
        openapi_examples={
            "default": {
                "summary": "A sample subject ID",
                "description": "Example subject ID for NSB Present",
                "value": "790025",
            }
        },
    ),
    settings=Depends(get_settings),
):
    """
    # NSB Present Endpoint
    Retrieve information from the NSB 2023-Present list for a given subject ID.
    """

    nsb_present_list = await get_nsb_present_list(
        subject_id=subject_id, settings=settings
    )
    nsb_present_models = [
        NSB2023List.model_validate(item["fields"]) for item in nsb_present_list
    ]
    return nsb_present_models
