# coding: utf-8

"""
    aind-sharepoint-service

     ## aind-sharepoint-service  Service to pull data from Sharepoint.  

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NSB2023Burr5PerformDuring(str, Enum):
    """
    Enum class for Burr5 Perform During.
    """

    """
    allowed enum values
    """
    INITIAL_SURGERY = 'Initial Surgery'
    FOLLOW_UP_SURGERY = 'Follow up Surgery'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NSB2023Burr5PerformDuring from a JSON string"""
        return cls(json.loads(json_str))


