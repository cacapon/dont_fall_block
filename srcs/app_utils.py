import pyxel
from .config import Vector2i

def get_block_size(block:list[list[str | None]])-> Vector2i:
	size = Vector2i(0, 0)
	for y, row in enumerate(block):
		for x, cell in enumerate(row):
			if cell is not None:
				size.y = max(size.y, y)
				size.x = max(size.x, x)
	size.x += 1
	size.y += 1
	print(f"size={size}")
	return size


# 中央揃えにするため、xはtext_len x 4pixelずらして出力します。
def text_center(x: float, y: float, s: str, col: int, font: pyxel.Font | None = None) -> None:
	_x = (pyxel.width - len(s) * 4) // 2
	pyxel.text(_x, y, s, col, font)