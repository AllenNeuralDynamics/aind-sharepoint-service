"""Module to retrieve data from a Sharepoint using a session object"""

import logging
from typing import Any, Optional
from pydantic import ValidationError, ValidatorFunctionWrapHandler
from aind_sharepoint_service_server.client import SharePointClient
from aind_sharepoint_service_server.models import LASList


class SessionHandler:
    """Handle session object to get data"""

    def __init__(self, session: SharePointClient):
        """Class constructor"""
        self.session = session

    def get_las_2020_procedures(self, subject_id: str):
        """
        Retrieve procedure info from LAS 2020 list for a given subject ID.
        Parameters
        ----------
        subject_id : str
            Subject ID to filter the procedures.
        Returns
        -------
        List[LASList]
            A list of LASList models containing the procedure information.
        """
        logging.info(f"Pulling data from LAS 2020 for {subject_id}")
        all_items = self.session._fetch_all_list_items(
            site_id=self.session.las_site_id,
            list_id=self.session.las_2020_list_id,
            subject_id=subject_id,
        )
        las_models = [
            LASList.model_validate(item["fields"]) for item in all_items
        ]
        return las_models
        
    
