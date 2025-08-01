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


class NSB2023AindProjectName(str, Enum):
    """
    Enum class for AIND Project Name.
    """

    """
    allowed enum values
    """
    BRAIN__WIDE__CIRCUIT__DYN = 'Brain Wide Circuit Dynamics'
    CELL__TYPE__LOOKUP__TABLE = 'Cell Type Lookup Table'
    COGNITIVE_FLEXIBILITY_IN = 'Cognitive flexibility in patch foraging'
    CREDIT_ASSIGNMENT_DURING = 'Credit assignment during learning (Brain Computer Interface)'
    DYNAMIC__ROUTING = 'Dynamic Routing'
    FORCE__FORGING = 'Force Forging'
    GENETIC__PERTURBATION__PR = 'Genetic Perturbation Project (GPP)'
    INDICATOR__TESTING = 'Indicator Testing'
    INFORMATION_SEEKING_IN_PA = 'Information seeking in partially observable environments'
    MEDULLA = 'Medulla'
    MULTIPLEXED_NM = 'Multiplexed NM'
    NEUROMODULATOR_CIRCUIT_DY = 'Neuromodulator circuit dynamics during foraging'
    OPEN_SCOPE = 'OpenScope'
    OPHYS_M_FISH__CELL_TYPES = 'Ophys mFISH* \"Cell types and learning\"'
    PLACE = 'PLACE'
    SINGLE__NEURON__COMPUTATI = 'Single-Neuron Computations within Brain-Wide Circuits (SCBC)*'
    THALAMUS = 'Thalamus'
    THALAMUS_AIND__SCIENTIFIC = 'Thalamus - AIND Scientific Activites'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NSB2023AindProjectName from a JSON string"""
        return cls(json.loads(json_str))


