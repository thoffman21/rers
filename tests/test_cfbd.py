"""
Tests for validating the connecion to and existence of the underlying data
that RERS is based on
"""

import cfbd
from rers import get_cfbd


def test_get_cfbd():
    cfbd.GamesApi(get_cfbd.configure_cfbd()).get_games(year=2022, season_type="regular")


def test_cfbd_teams():
    """
    Check each team (both FBS and non-FBS) for valid data
    """
    teams_api = cfbd.TeamsApi(get_cfbd.configure_cfbd())
    fbs_teams = teams_api.get_fbs_teams(year=2022)
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

    print(
        f"There are {len(bad_fbs_teams)} bad FBS teams \
            and {len(bad_all_teams)} bad total teams"
    )


test_cfbd_teams()
