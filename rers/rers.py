import random

import cfbd
from prettytable import PrettyTable

from rers import elo, get_cfbd


class Team:
    def __init__(self, cfbd_team: cfbd.Team) -> None:
        self._cfbd_team = cfbd_team
        self.name = cfbd_team.school
        self.elo_rating = 1000
        self.initial_elo_rating = 1000


class Ranking:
    def __init__(self, year: int = 2022) -> None:
        self.teams = generate_teams(year)

    def initialize_rankings(self, method: str = None):
        if method == "random":
            for team in self.teams:
                team.elo_rating = random.randint(800, 1200)

    def generate_rankings(self, through_week: int = -1):
        pass

    def print_rankings(self, show_through: int = 25):
        teams_sorted = sorted(self.teams, key=lambda x: x.elo_rating, reverse=True)

        table = PrettyTable(["Rank", "Team", "Elo Rating"])
        for i, team in enumerate(teams_sorted[0:show_through]):
            table.add_row([i + 1, team._cfbd_team.school, team.elo_rating])
        print(table)


def generate_teams(year: int = 2023) -> list:
    return [Team(team) for team in get_cfbd.get_teams(year=year)]


def calculate_expected_outcome(
    home_team: Team, away_team: Team, neutral_site: bool = False
) -> tuple[float, float]:
    home_expect = elo.calc_expected_outcome(home_team.elo_rating, away_team.elo_rating)
    away_expect = 1 - home_expect

    return home_expect, away_expect
