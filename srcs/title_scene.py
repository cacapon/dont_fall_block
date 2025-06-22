import pyxel
from srcs.base_scene import BaseScene 
from .pyxel_utils import text_center
from .config import GAMEMODE, WINDOW_W, WINDOW_H


class TitleScene(BaseScene):
    def update(self) -> GAMEMODE:
        if pyxel.btnp(pyxel.KEY_SPACE):
            return GAMEMODE.Game
        return GAMEMODE.Title

	# TODO
    def draw(self):
        title_pos = 60
        text_center(WINDOW_W // 2, title_pos, "don't", 7)
        text_center(WINDOW_W // 2, title_pos + 12, "fall", 7)
        text_center(WINDOW_W // 2, title_pos + 24, "blocks", 7)
        text_center(WINDOW_W // 2, WINDOW_H - 24, "PRESS SPACE KEY", 7)
