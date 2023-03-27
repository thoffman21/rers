import cfbd

from rers import __version__, get_cfbd


def test_version():
    assert __version__ == "0.1.0"


def test_get_cfbd():
    cfbd.GamesApi(get_cfbd.configure_cfbd()).get_games(year=2022, season_type="regular")
