"""Core models used across packages."""

from typing import Any, Literal, Optional

from pydantic import BaseModel, ValidationError
from pydantic_core.core_schema import ValidatorFunctionWrapHandler

from aind_sharepoint_service_server import __version__


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


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: Literal["OK"] = "OK"
    service_version: str = __version__
