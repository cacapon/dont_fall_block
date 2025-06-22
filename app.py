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
		self.my_score = 0
		self.game_mode = GAMEMODE.Title
		self.game_scene = {
			GAMEMODE.Title: 	TitleScene(),
			GAMEMODE.Game:		GameScene(),
			GAMEMODE.Result:	ResultScene(), 
		}
		pyxel.run(self.update, self.draw)
	
	def update(self):
		try:
			self.game_mode = self.game_scene[self.game_mode].update()
		except:
			print("update failed: Invalid game mode:", self.game_mode)
			self.game_mode = GAMEMODE.Title

	def draw(self):
		pyxel.cls(0)
		try:
			self.game_scene[self.game_mode].draw()
		except:
			print("draw failed: Invalid game mode:", self.game_mode)
			self.game_mode = GAMEMODE.Title

if __name__ == '__main__':
	App()