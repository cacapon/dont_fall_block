import pyxel
from random import choice
from srcs.base_scene import BaseScene
from .config import GAMEMODE, IMAGE_ID, BLOCK_SIZE, Vector2i, FPS, Timer, BLOCK
from .app_utils import get_block_size

STAGE_SIZE = Vector2i(10, 20)
BLOCK_TYPE = ["Z", "T", "O", "S", "L", "I", "J"]
IMAGE_MAP = {
	"Z": Vector2i(0, 0),
	"T": Vector2i(0, 8),
	"O": Vector2i(8, 0),
	"S": Vector2i(8, 8),
	"L": Vector2i(16, 0),
	"I": Vector2i(16, 8),
	"J": Vector2i(24, 0),
	"WALL": Vector2i(24, 8),
	None: Vector2i(32, 0),
}


# utils
def clampi(value: int, min_value: int, max_value: int):
	return max(min_value, min(value, max_value))


class GameScene(BaseScene):
	def __init__(self, high_score):
		self.high_score = high_score
		self.score = 0
		self.timer = Timer(1, 0)
		self.stage = self._gen_stage() 
		self.mouse_click_count = 0
		self.pos = Vector2i(0, 0)
		self.my_block_type = choice(BLOCK_TYPE)
		self.my_block =  BLOCK[self.my_block_type][self.mouse_click_count]
		self.is_timeup = False
		self.show_mv_block = True

	def _gen_stage(self):
		stage =  [self._gen_line() for _ in range(STAGE_SIZE.y)]
		for _ in range(4):
			stage.append(["GUARD"] * STAGE_SIZE.x)
		return stage

	def _gen_line(self):
		line = [None] * (STAGE_SIZE.x + 4)
		for i in range(4):
			line[STAGE_SIZE.x + i] = "GUARD"
		return line

	def update(self) -> GAMEMODE:
		gamemode = GAMEMODE.Game
		if self.is_timeup is True:
			return GAMEMODE.Result
		self._set_pos()
		self._count_down_timer()
		gamemode = self._on_pressed()
		self._line_remove()
		return gamemode

	def _set_pos(self):
		x = pyxel.mouse_x // BLOCK_SIZE.x
		y = pyxel.mouse_y // BLOCK_SIZE.y
		self.pos.x = clampi(x, 0, STAGE_SIZE.x - get_block_size(self.my_block).x)
		self.pos.y = clampi(y, 0, STAGE_SIZE.y - get_block_size(self.my_block).y)
		print(self.pos)

	def _count_down_timer(self):
		if pyxel.frame_count % FPS != 0:
			return
		if self.timer.m + self.timer.s == 0:
			self.is_timeup = True
			return
		self.timer.s -= 1
		if self.timer.s < 0:
			self.timer.m -= 1
			self.timer.s = 59

	def _on_pressed(self):
		if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
			pyxel.play(0, 8)
			self.mouse_click_count = (self.mouse_click_count - 1) % 4
			self.my_block = BLOCK[self.my_block_type][self.mouse_click_count]
		if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
			pyxel.play(0, 8)
			self.mouse_click_count = (self.mouse_click_count + 1) % 4
			self.my_block = BLOCK[self.my_block_type][self.mouse_click_count]
		if pyxel.btnp(pyxel.KEY_SPACE):
			self._fix_block()
		if pyxel.btnp(pyxel.KEY_Q):
			return GAMEMODE.Result
		return GAMEMODE.Game

	def _fix_block(self):
		if not self._can_fix(self.my_block):
			pyxel.play(0, 5)
			return
		for y in range(len(self.my_block)):
			for x in range(len(self.my_block[y])):
				if self.my_block[y][x] == None:
					continue
				self.stage[y + self.pos.y][x + self.pos.x] = self.my_block[y][x]
		pyxel.play(0, 6)
		self.mouse_click_count = 0
		self.my_block_type = choice(BLOCK_TYPE)
		self.my_block = BLOCK[self.my_block_type][self.mouse_click_count]

	def _can_fix(self, block:list[list[str | None]]) -> bool:
		for y in range(len(block)):
			for x in range(len(block[y])):
				if block[y][x] is None:
					continue
				if self.stage[y + self.pos.y][x + self.pos.x] is not None:
					return False
		return True

	def _line_remove(self):
		rm_count = 0
		for i, line in enumerate(self.stage):
			if line[0] == "GUARD":
				continue
			if None not in line:
				rm_count += 1
				self.stage.pop(i)
				self.stage.insert(i, self._gen_line())
		if rm_count == 0:
			return
		self.score += 100 * (2 ** (rm_count - 1))
		if (self.score > self.high_score):
			self.high_score = self.score
		pyxel.play(0, 7)

	def draw(self):
		self._draw_score_area()
		self._draw_stage()
		self._draw_move_block()

	def _draw_score_area(self):
		pyxel.text(85, 10, "HIGH SCORE:{}".format(self.high_score), 7)
		pyxel.text(85, 20, "     SCORE:{}".format(self.score), 7)
		pyxel.text(85, 30, "TIME:{}:{:0=2}".format(self.timer.m, self.timer.s), 7)

		pyxel.text(85, 50, "LEFT_SPIN:", 7)
		pyxel.blt(85, 60, IMAGE_ID.BLOCK.value, 40, 0, BLOCK_SIZE.x * 2, BLOCK_SIZE.y * 2)
		pyxel.text(85, 80, "RIGHT_SPIN:", 7)
		pyxel.blt(85, 90, IMAGE_ID.BLOCK.value, 56, 0, BLOCK_SIZE.x * 2, BLOCK_SIZE.y * 2)
		pyxel.text(85, 110, "FIX:", 7)
		pyxel.blt(102, 108, IMAGE_ID.BLOCK.value, 72, 0, BLOCK_SIZE.x * 2, BLOCK_SIZE.y)
		pyxel.text(85, 130, "GIVEUP: Q key", 7)

	def _draw_stage(self):
		for y in range(STAGE_SIZE.y):
			for x in range(STAGE_SIZE.x):
				if self.stage[y][x] is None or self.stage[y][x] == "GUARD":
					block = IMAGE_MAP.get(None)
				else:
					block = IMAGE_MAP.get(self.stage[y][x])
				pyxel.blt(x * BLOCK_SIZE.x, y * BLOCK_SIZE.y,
					IMAGE_ID.BLOCK.value,
					block.x, block.y, BLOCK_SIZE.x, BLOCK_SIZE.y, 10,
				)

	def _draw_move_block(self):
		if pyxel.frame_count % 15 == 0:
			self.show_mv_block = not self.show_mv_block
		if not self.show_mv_block:
			return
		for y, block_row in enumerate(self.my_block):
			for x, block_cell in enumerate(block_row):
				if block_cell == None:
					continue
				block_map = IMAGE_MAP.get(block_cell)
				draw_pos = Vector2i((x + self.pos.x) * BLOCK_SIZE.x, (y + self.pos.y) * BLOCK_SIZE.y)
				pyxel.blt(draw_pos.x, draw_pos.y,
					IMAGE_ID.BLOCK.value,
					block_map.x, block_map.y, BLOCK_SIZE.x, BLOCK_SIZE.y, 10,
				)