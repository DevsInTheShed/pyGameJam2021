from enum import Enum

class Action(Enum):
    idle = 0
    run = 1
    jump = 2
    death = 3

class Screen(Enum):
    menu = 0
    intro = 1
    stage = 2
    end = 3
    credits = 4

class Level(Enum):
    none = 0
    one = 1
    two = 2
    three = 3
    four = 4
