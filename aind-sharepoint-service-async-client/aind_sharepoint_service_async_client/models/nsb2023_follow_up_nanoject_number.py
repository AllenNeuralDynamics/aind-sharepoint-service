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


class NSB2023FollowUpNanojectNumber(str, Enum):
    """
    Enum class for Follow up Nanoject Number.
    """

    """
    allowed enum values
    """
    SELECT = 'Select...'
    NJ_1 = 'NJ#1'
    NJ_2 = 'NJ#2'
    NJ_3 = 'NJ#3'
    NJ_4 = 'NJ#4'
    NJ_5 = 'NJ#5'
    NJ_6 = 'NJ#6'
    NJ_7 = 'NJ#7'
    NJ_8 = 'NJ#8'
    N_A = 'N/A'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NSB2023FollowUpNanojectNumber from a JSON string"""
        return cls(json.loads(json_str))


