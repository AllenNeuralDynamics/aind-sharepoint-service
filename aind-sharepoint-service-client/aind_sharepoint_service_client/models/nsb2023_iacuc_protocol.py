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


class NSB2023IacucProtocol(str, Enum):
    """
    Enum class for IACUC NSB2023Protocol.
    """

    """
    allowed enum values
    """
    SELECT = 'Select...'
    N_2117 = '2117'
    N_2201 = '2201'
    N_2202 = '2202'
    N_2205 = '2205'
    N_2212 = '2212'
    N_2301 = '2301'
    N_2304 = '2304'
    N_2305 = '2305'
    N_2306 = '2306'
    N_2307 = '2307'
    N_2401 = '2401'
    N_2402 = '2402'
    N_2403 = '2403'
    N_2404 = '2404'
    N_2405 = '2405'
    N_2406 = '2406'
    N_2410 = '2410'
    N_2412 = '2412'
    N_2413 = '2413'
    N_2414 = '2414'
    N_2415 = '2415'
    N_2416 = '2416'
    N_2418 = '2418'
    N_2427 = '2427'
    N_1906 = '1906'
    N_2001 = '2001'
    N_2003 = '2003'
    N_2004 = '2004'
    N_2005 = '2005'
    N_2006 = '2006'
    N_2011 = '2011'
    N_2102 = '2102'
    N_2103 = '2103'
    N_2104 = '2104'
    N_2105 = '2105'
    N_2106 = '2106'
    N_2107 = '2107'
    N_2108 = '2108'
    N_2109 = '2109'
    N_2110 = '2110'
    N_2113 = '2113'
    N_2115 = '2115'
    N_2010 = '2010'
    N_2119 = '2119'
    N_2204 = '2204'
    N_2207 = '2207'
    N_2308 = '2308'
    N_2417 = '2417'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NSB2023IacucProtocol from a JSON string"""
        return cls(json.loads(json_str))


