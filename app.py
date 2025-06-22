import pyxel
from srcs.config import WINDOW_SIZE, FPS, GAMEMODE
from srcs.title_scene import TitleScene
from srcs.game_scene import GameScene
from srcs.result_scene import ResultScene

class App():
	def __init__(self):
		pyxel.init(WINDOW_SIZE.x, WINDOW_SIZE.y, fps=FPS)
		pyxel.load('assets/app.pyxres')
		self.high_score = 0
		self.game_mode = GAMEMODE.Title
		self.current_scene = TitleScene()
		pyxel.run(self.update, self.draw)
	
	def update(self):
		next_mode = self.current_scene.update()
		if next_mode != self.game_mode:
			self._switch_scene(next_mode)
		self.game_mode = next_mode
	
	def _switch_scene(self, next_mode):
		if next_mode == GAMEMODE.Title:
			self.current_scene = TitleScene()
		elif next_mode == GAMEMODE.Game:
			self.current_scene = GameScene(self.high_score)
		elif next_mode == GAMEMODE.Result:
			if hasattr(self.current_scene, "score"):
				score = self.current_scene.score
			else:
				score = 0
			if hasattr(self.current_scene, "high_score"):
				self.high_score = self.current_scene.high_score
			else:
				high_score = 0
			self.current_scene = ResultScene(score, self.high_score)

	def draw(self):
		pyxel.cls(0)
		self.current_scene.draw()

if __name__ == '__main__':
	App()