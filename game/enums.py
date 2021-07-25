from enum import Enum


class Action(Enum):
    idle = 0
    run = 1
    jump = 2

class Screen(Enum):
    menu = 0
    intro = 1
    stage = 2
    end = 3
    credits = 4