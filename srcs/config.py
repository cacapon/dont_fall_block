from enum import Enum, auto
from dataclasses import dataclass

@dataclass
class Vector2:
    x: float
    y: float

@dataclass
class Vector2i:
    x: int
    y: int

@dataclass
class Timer:
    m: int
    s: int

WINDOW_SIZE = Vector2i(150, 200)
BLOCK_SIZE = Vector2i(8, 8)
FPS = 30

class IMAGE_ID(Enum):
    BLOCK = 0
    FIX_BLOCK = 1

class GAMEMODE(Enum):
    Title = auto()
    Game = auto()
    Result = auto()


BLOCK = {
    "Z": [
        [
            ["Z", "Z", None, None],
            [None, "Z", "Z", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, "Z", None, None],
            ["Z", "Z", None, None],
            ["Z", None, None, None],
            [None, None, None, None],
        ],
        [
            ["Z", "Z", None, None],
            [None, "Z", "Z", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, "Z", None, None],
            ["Z", "Z", None, None],
            ["Z", None, None, None],
            [None, None, None, None],
        ],
    ],
    "T": [
        [
            ["T", "T", "T", None],
            [None, "T", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, "T", None, None],
            ["T", "T", None, None],
            [None, "T", None, None],
            [None, None, None, None],
        ],
        [
            [None, "T", None, None],
            ["T", "T", "T", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["T", None, None, None],
            ["T", "T", None, None],
            ["T", None, None, None],
            [None, None, None, None],
        ],
    ],
    "O": [
        [
            ["O", "O", None, None],
            ["O", "O", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["O", "O", None, None],
            ["O", "O", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["O", "O", None, None],
            ["O", "O", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["O", "O", None, None],
            ["O", "O", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
    ],
    "S": [
        [
            [None, "S", "S", None],
            ["S", "S", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["S", None, None, None],
            ["S", "S", None, None],
            [None, "S", None, None],
            [None, None, None, None],
        ],
        [
            [None, "S", "S", None],
            ["S", "S", None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["S", None, None, None],
            ["S", "S", None, None],
            [None, "S", None, None],
            [None, None, None, None],
        ],
    ],
    "L": [
        [
            ["L", None, None, None],
            ["L", None, None, None],
            ["L", "L", None, None],
            [None, None, None, None],
        ],
        [
            ["L", "L", "L", None],
            ["L", None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["L", "L", None, None],
            [None, "L", None, None],
            [None, "L", None, None],
            [None, None, None, None],
        ],
        [
            [None, None, "L", None],
            ["L", "L", "L", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
    ],
    "I": [
        [
            ["I", None, None, None],
            ["I", None, None, None],
            ["I", None, None, None],
            ["I", None, None, None],
        ],
        [
            ["I", "I", "I", "I"],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["I", None, None, None],
            ["I", None, None, None],
            ["I", None, None, None],
            ["I", None, None, None],
        ],
        [
            ["I", "I", "I", "I"],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
    ],
    "J": [
        [
            [None, "J", None, None],
            [None, "J", None, None],
            ["J", "J", None, None],
            [None, None, None, None],
        ],
        [
            ["J", None, None, None],
            ["J", "J", "J", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            ["J", "J", None, None],
            ["J", None, None, None],
            ["J", None, None, None],
            [None, None, None, None],
        ],
        [
            ["J", "J", "J", None],
            [None, None, "J", None],
            [None, None, None, None],
            [None, None, None, None],
        ],
    ],
}
