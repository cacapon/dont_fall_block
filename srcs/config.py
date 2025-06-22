from enum import Enum, auto

WINDOW_W = 150
WINDOW_H = 200
FPS = 30


class GAMEMODE(Enum):
    Title = auto()
    Game = auto()
    Result = auto()


BLOCK = {
    "Z": [
        [
            ["Z", "Z", "EMP", "EMP"],
            ["EMP", "Z", "Z", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "Z", "EMP", "EMP"],
            ["Z", "Z", "EMP", "EMP"],
            ["Z", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["Z", "Z", "EMP", "EMP"],
            ["EMP", "Z", "Z", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "Z", "EMP", "EMP"],
            ["Z", "Z", "EMP", "EMP"],
            ["Z", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "T": [
        [
            ["T", "T", "T", "EMP"],
            ["EMP", "T", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "T", "EMP", "EMP"],
            ["T", "T", "EMP", "EMP"],
            ["EMP", "T", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "T", "EMP", "EMP"],
            ["T", "T", "T", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["T", "EMP", "EMP", "EMP"],
            ["T", "T", "EMP", "EMP"],
            ["T", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "O": [
        [
            ["O", "O", "EMP", "EMP"],
            ["O", "O", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["O", "O", "EMP", "EMP"],
            ["O", "O", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["O", "O", "EMP", "EMP"],
            ["O", "O", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["O", "O", "EMP", "EMP"],
            ["O", "O", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "S": [
        [
            ["EMP", "S", "S", "EMP"],
            ["S", "S", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["S", "EMP", "EMP", "EMP"],
            ["S", "S", "EMP", "EMP"],
            ["EMP", "S", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "S", "S", "EMP"],
            ["S", "S", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["S", "EMP", "EMP", "EMP"],
            ["S", "S", "EMP", "EMP"],
            ["EMP", "S", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "L": [
        [
            ["L", "EMP", "EMP", "EMP"],
            ["L", "EMP", "EMP", "EMP"],
            ["L", "L", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["L", "L", "L", "EMP"],
            ["L", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["L", "L", "EMP", "EMP"],
            ["EMP", "L", "EMP", "EMP"],
            ["EMP", "L", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["EMP", "EMP", "L", "EMP"],
            ["L", "L", "L", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "I": [
        [
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
        ],
        [
            ["I", "I", "I", "I"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
            ["I", "EMP", "EMP", "EMP"],
        ],
        [
            ["I", "I", "I", "I"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
    "J": [
        [
            ["EMP", "J", "EMP", "EMP"],
            ["EMP", "J", "EMP", "EMP"],
            ["J", "J", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["J", "EMP", "EMP", "EMP"],
            ["J", "J", "J", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["J", "J", "EMP", "EMP"],
            ["J", "EMP", "EMP", "EMP"],
            ["J", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
        [
            ["J", "J", "J", "EMP"],
            ["EMP", "EMP", "J", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
            ["EMP", "EMP", "EMP", "EMP"],
        ],
    ],
}
