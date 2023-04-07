from rers import __version__, rers, get_cfbd


def test_version():
    assert __version__ == "0.1.0"


def test_team_class():
    team = rers.Team(get_cfbd.get_random_team(year=2023))
    assert team is not None


def test_ranking_class():
    ranking = rers.Ranking()
    ranking.initialize_rankings(method="random")


def test_print_rankings():
    ranking = rers.Ranking()
    ranking.initialize_rankings(method="random")
    ranking.print_rankings()
