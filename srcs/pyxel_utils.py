import pyxel

# 中央揃えにするため、xはtext_len x 4pixelずらして出力します。
def text_center(x: float, y: float, s: str, col: int, font: pyxel.Font | None = None) -> None:
	_x = (pyxel.width - len(s) * 4) // 2
	pyxel.text(_x, y, s, col, font)