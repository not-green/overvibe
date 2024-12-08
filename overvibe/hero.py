"""
Definitions of all Heros.
"""

from typing import TypeAlias
import enum


@enum.unique
class Category(enum.Enum):
    """
    A Hero Category/Class.
    """

    TANK = 0
    DAMAGE = 1
    SUPPORT = 2


Hero: TypeAlias = tuple[str, Category]

HEROES: frozenset[Hero] = frozenset(
    [
        # TANK HEROES
        ("d.va", Category.TANK),
        ("doomfist", Category.TANK),
        ("junker queen", Category.TANK),
        ("mauga", Category.TANK),
        ("orisa", Category.TANK),
        ("ramattra", Category.TANK),
        ("reinhardt", Category.TANK),
        ("roadhog", Category.TANK),
        ("sigma", Category.TANK),
        ("winston", Category.TANK),
        ("wrecking ball", Category.TANK),
        ("zarya", Category.TANK),
        # DAMAGE HEROES
        ("ashe", Category.DAMAGE),
        ("bastion", Category.DAMAGE),
        ("cassidy", Category.DAMAGE),
        ("echo", Category.DAMAGE),
        ("genji", Category.DAMAGE),
        ("hanzo", Category.DAMAGE),
        ("junkrat", Category.DAMAGE),
        ("mei", Category.DAMAGE),
        ("pharah", Category.DAMAGE),
        ("reaper", Category.DAMAGE),
        ("soldier: 76", Category.DAMAGE),
        ("sombra", Category.DAMAGE),
        ("sojourn", Category.DAMAGE),
        ("symmetra", Category.DAMAGE),
        ("torbjörn", Category.DAMAGE),
        ("tracer", Category.DAMAGE),
        ("venture", Category.DAMAGE),
        ("widowmaker", Category.DAMAGE),
        # SUPPORT HEROES
        ("ana", Category.SUPPORT),
        ("baptiste", Category.SUPPORT),
        ("brigitte", Category.SUPPORT),
        ("illari", Category.SUPPORT),
        ("juno", Category.SUPPORT),
        ("kiriko", Category.SUPPORT),
        ("lifeweaver", Category.SUPPORT),
        ("lúcio", Category.SUPPORT),
        ("mercy", Category.SUPPORT),
        ("moira", Category.SUPPORT),
        ("zenyatta", Category.SUPPORT),
    ]
)
