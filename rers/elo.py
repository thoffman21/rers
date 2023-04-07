"""
Functions for handling the core Elo rating calculations,
or how actual outcomes are determined
"""


def calc_expected_outcome(
    player_rating: float, opponent_rating: float, E: float = 400
) -> float:
    """
    Calculate expected outcome, between 0 and 1, between two players. The opponent
    outcome will be 1 - calc_expected_outcome()

    Parameters
    ----------
    player_rating : float
        A player's Elo rating
    opponent_rating : float
        Opponent's Elo rating
    E : float, optional
        Constant that adjusts much expectations should correlate to differences in
        rating , by default 400

    Returns
    -------
    float
        The expected outcome for the player. The opponent's expected outcome is
        1 - this value.
    """

    return 1 / (1 + 10 ** ((opponent_rating - player_rating) / E))


def calc_rating_change(
    actual_outcome: float, expected_outcome: float, K: float = 32
) -> float:
    """
    Calculate the rating change for a player based on their actual and expected outcome

    Parameters
    ----------
    actual_outcome : float
        The outcome, between 0 and 1. This is agnostic of how this outcome is determined
    expected_outcome : float
        Expected outcome for this player, should be found based on respective ratings
    K : float, optional
        The sensitivity factor, effecting how much the rating is impacted, by default 32

    Returns
    -------
    float
        The change (+ or -) to this player's rating
    """
    return K * (actual_outcome - expected_outcome)
