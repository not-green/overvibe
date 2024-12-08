"""
Game State tracking definitions.

Shared module definitions of the active game state such that producers can
create these definitions for consumers to use.
"""

from typing import TypeAlias, TypeVar
import dataclasses

from overvibe.hero import Hero

T = TypeVar("T")

# represents a value which may or may not be determinable
MaybeDefinable: TypeAlias = T | None


@dataclasses.dataclass
class Playing:
    """
    Player is Playing.
    """

    hero: MaybeDefinable[Hero]


@dataclasses.dataclass
class InMenu:
    """
    Player is in a Menu.
    """


State: TypeAlias = Playing | InMenu


@dataclasses.dataclass
class Game:
    """
    Main Game State.
    """

    state: State
