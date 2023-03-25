from rers import elo


def test_elo_functions():
    player_rating = 1613
    cum_change = 0
    for opp_rating, outcome in zip([1609, 1477, 1388, 1586, 1720], [0, 0.5, 1, 1, 0]):
        expected_outcome = elo.calc_expected_outcome(player_rating, opp_rating)
        cum_change += elo.calc_rating_change(outcome, expected_outcome)

    player_rating += cum_change
    # This should be very close to 1601
    assert abs(player_rating - 1601) < 1
