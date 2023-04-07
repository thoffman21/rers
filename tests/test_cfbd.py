"""
Tests for validating the connecion to and existence of the underlying data
that RERS is based on
"""

import cfbd
from rers import get_cfbd
import pytest


def test_get_cfbd():
    cfbd.GamesApi(get_cfbd.configure_cfbd()).get_games(year=2022, season_type="regular")


@pytest.mark.parametrize("year,n_fbs_teams", [(2023, 131), (2022, 131), (2021, 130)])
def test_get_cfbd_teams(year, n_fbs_teams):
    """
    Check each team (both FBS and non-FBS) for valid data, assert that the number
    of FBS teams returned matches expectation
    """
    teams_api = cfbd.TeamsApi(get_cfbd.configure_cfbd())
    fbs_teams = teams_api.get_fbs_teams(year=year)
    all_teams = teams_api.get_teams()

    bad_fbs_teams = []
    for team in fbs_teams:
        if not (team.school is not None and team.school != "") and not (
            team.conference is not None and team.conference != ""
        ):
            bad_fbs_teams.append(team)

    bad_all_teams = []
    for team in all_teams:
        if not (team.school is not None and team.school != "") and not (
            team.conference is not None and team.conference != ""
        ):
            bad_all_teams.append(team)

    assert len(fbs_teams) == n_fbs_teams
