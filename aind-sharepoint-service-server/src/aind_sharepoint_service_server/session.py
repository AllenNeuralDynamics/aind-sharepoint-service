"""Module to handle requests session"""

from aind_sharepoint_service_server.configs import Settings
from aind_sharepoint_service_server.client import SharePointClient

settings = Settings()


def get_session():
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    yield SharePointClient.from_settings(settings=settings)
