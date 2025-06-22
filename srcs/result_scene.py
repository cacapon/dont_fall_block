import pyxel
from srcs.base_scene import BaseScene 
from .config import GAMEMODE, WINDOW_SIZE
from .app_utils import text_center

class ResultScene(BaseScene):
    def __init__(self, score, high_score):
        self.score = score
        self.high_score = high_score
        
    def update(self) -> GAMEMODE:
        if pyxel.btnp(pyxel.KEY_SPACE):
            return GAMEMODE.Title
        return GAMEMODE.Result

    def draw(self):
        text_center(WINDOW_SIZE.x // 2, 12, "Result", 7)
        text_center(WINDOW_SIZE.x // 2, 24, f"HIGH:{self.high_score}", 7)
        text_center(WINDOW_SIZE.x // 2, 36, f"HIGH:{self.score}", 7)
        text_center(WINDOW_SIZE.x // 2, WINDOW_SIZE.y - 12, "PRESS SPACE KEY", 7)

