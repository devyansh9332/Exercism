
"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Return True if Pac-Man can eat a ghost."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Return True if Pac-Man touches a power pellet or a dot."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Return True if Pac-Man touches a ghost without an active power pellet."""
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Return True if Pac-Man has eaten all dots without losing."""
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
