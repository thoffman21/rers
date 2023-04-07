import cfbd
import elo


class Team:
    def __init__(self, cfbd_team: cfbd.Team) -> None:
        self._cfbd_team = cfbd_team
        self.elo_rating = 1000
        self.initial_elo_rating = 1000


def calculate_expected_outcome(
    home_team: Team, away_team: Team, neutral_site: bool = False
) -> tuple[float, float]:
    home_expect = elo.calc_expected_outcome(home_team.elo_rating, away_team.elo_rating)
    away_expect = 1 - home_expect

    return home_expect, away_expect
