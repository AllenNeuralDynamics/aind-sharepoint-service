"""Module to handle endpoint responses"""

from fastapi import APIRouter, Depends, HTTPException, Path, status
from aind_sharepoint_service_server.handler import SessionHandler
from aind_sharepoint_service_server.models import HealthCheck
from aind_sharepoint_service_server.session import get_session
from aind_sharepoint_service_server.models import LASList
from typing import List

router = APIRouter()


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
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck()

@router.get(
    "/las2020_procedures/{subject_id}",
    response_model=List[LASList],
)
async def get_las_2020_procedures(
    subject_id: str = Path(..., examples=["805811"]),
    session: SessionHandler = Depends(get_session),
):
    """
    # LAS 2020 Procedures Endpoint
    Retrieve procedure information from the LAS 2020 list for a given subject ID.
    """
    las_procedures = SessionHandler(session=session).get_las_2020_procedures(subject_id)
    if not las_procedures:
        raise HTTPException(
            status_code=404,
            detail=f"No procedures found for subject ID {subject_id} in LAS 2020.",
        )
    else:
        return las_procedures

