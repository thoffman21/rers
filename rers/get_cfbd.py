import os

import cfbd
from dotenv import load_dotenv


def configure_cfbd(cfbd_api_key: str = None):
    """Configure general API connection to CFBD database"""

    # If user does not enter an API key, it should be in a top level .env
    # Or accessible via GitHub secrets
    if cfbd_api_key is None:
        load_dotenv()
        cfbd_api_key = os.getenv("CFBD_API_KEY")

    config = cfbd.Configuration()
    config.api_key["Authorization"] = cfbd_api_key
    config.api_key_prefix["Authorization"] = "Bearer"

    return cfbd.ApiClient(config)


def get_teams(
    year: int = 2023, fbs_only: bool = True, cfbd_api_client: cfbd.ApiClient = None
):
    if cfbd_api_client is None:
        cfbd_api_client = configure_cfbd()

    if fbs_only:
        return cfbd.TeamsApi(cfbd_api_client).get_fbs_teams(year=year)
    else:
        return cfbd.TeamsApi(cfbd_api_client).get_teams(year=year)
