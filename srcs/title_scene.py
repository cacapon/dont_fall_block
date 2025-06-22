import pyxel
from srcs.base_scene import BaseScene 
from .app_utils import text_center
from .config import GAMEMODE, WINDOW_SIZE


class TitleScene(BaseScene):
    def update(self) -> GAMEMODE:
        if pyxel.btnp(pyxel.KEY_SPACE):
            return GAMEMODE.Game
        return GAMEMODE.Title

	# TODO
    def draw(self):
        title_pos = 60
        text_center(WINDOW_SIZE.x // 2, title_pos, "don't", 7)
        text_center(WINDOW_SIZE.x // 2, title_pos + 12, "fall", 7)
        text_center(WINDOW_SIZE.x // 2, title_pos + 24, "block", 7)
        text_center(WINDOW_SIZE.x // 2, WINDOW_SIZE.y - 24, "PRESS SPACE KEY", 7)
