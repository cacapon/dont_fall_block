import pyxel
from random import choice
from copy import deepcopy

from assets import blockarr

'''
    # 記述ルール
        $name:type…変数:型
        $NAME…定数
        $name = X… Xで $name を初期化,もしくは代入
        $name[name.(個数,型)] …配列
        name() 関数

    # memo
    # スタンプ = 出来る。同じ画像ならbltで複数設定可能
    # スタンプの材料: スタンプ位置を覚えておく座標　flgを立てる処理 flgが経っているところだけ表示する処理
    # 一列そろったら消す処理: col.pop(n-1段目) col.insert(n-1段目, 空の段)
    # 消す段と判断するには？: その段に0がないか確認
    # 空の段 ['NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE']
    # ランダムでブロックを変える機能
'''

# $GLOBAL
WINDOW_W = 150    # $ウィンドウの幅 :int = 150
WINDOW_H = 200    # $ウィンドウの高さ :int = 200
STAGE_W = 10   # $ステージの幅 :int = 10
STAGE_H = 20    # $ステージの高さ :int = 20
BLOCK_WH = 8  # $ブロックの大きさ(正方形) :int = 8
MAP_TIP_WH = 4  # $ブロックのマップチップの大きさ(正方形) :int = 4
BLANK_AREA = MAP_TIP_WH - 1  # ブロック固定するときに想定される、ゲーム外領域
DEFAULT_FPS = 30

ENPTY_ROW = []    # $空の段['EMP'.($ステージの幅,int)]
for set_enpty_row in range(STAGE_W):
    ENPTY_ROW.append('EMP')
for set_brank_cell in range(BLANK_AREA):
    ENPTY_ROW.append('NONE')

BLANK_ROW = []
for set_blank_row in range(STAGE_W + BLANK_AREA):
    BLANK_ROW.append('NONE')


IMAGE_ID0 = 0  # ブロックの回転用の図柄
IMAGE_ID1 = 1  # タイムアップ画面

# ブロックの種類 dict型にしたけど書き方あってるかな…
# 使い方の例: IMAGE_POINTS.get('EMP').get('W')
IMAGE_POINTS = {
    # BLOCK_NAME = ロードしてきたmapの座標[W,H]
    'Z'   : {'W':  0, 'H': 0},
    'T'   : {'W':  0, 'H': 8},
    'O'   : {'W':  8, 'H': 0},
    'S'   : {'W':  8, 'H': 8},
    'L'   : {'W': 16, 'H': 0},
    'I'   : {'W': 16, 'H': 8},
    'J'   : {'W': 24, 'H': 0},
    'WALL': {'W': 24, 'H': 8},
    'EMP' : {'W': 32, 'H': 0},
    'NONE': {'W': 32, 'H': 8},
}


class App():
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, fps=DEFAULT_FPS)    # ウィンドウの幅、高さでpyxelの初期化
        pyxel.load('assets/app.pyxres')    # ブロックの画像を読み込む

        self.game_init()

        self.high_score = 0
        self.my_score = 0
        pyxel.run(self.update, self.draw)

    def game_init(self):
        self.stage = []  # $ステージの配列[列.($ステージの高さ,int)][行.($ステージの高さ,int)] = 'NONE'で初期化
        for set_stage in range(STAGE_H):
            self.stage.append(deepcopy(ENPTY_ROW))
        for set_blank in range(BLANK_AREA):
            self.stage.append(deepcopy(BLANK_ROW))

        self.count_right_mouth_click = 0  # $右クリック数:int = 0
        self.point_move_block = {'W': 0, 'H': 0}  # $動かせるブロックの位置:[横:int,縦:int] = [0,0]
        self.block_vector = {0: {'W': 0, 'H': 0}, 1: {'W': 4, 'H': 0}, 2: {'W': 4, 'H': 4}, 3: {'W': 0, 'H': 4}}  # これとcount_right_mouth_clickの数値から、画像の向きを取得する
        self.my_block = choice(['Z', 'T', 'O', 'S', 'L', 'I', 'J'])
        self.timer = [2, 0]
        self.timeup = False

    def update(self):
        if self.timeup is True:
            self.update_timeup_mode()
            return

        self.point_move_block['W'] = pyxel.mouse_x // BLOCK_WH  # 動作ブロックの動き(横) = ブロックの大きさ * (pyxel.mouse_x // ブロックの大きさ)
        self.point_move_block['H'] = pyxel.mouse_y // BLOCK_WH  # 動作ブロックの動き(縦) = ブロックの大きさ * (pyxel.mouse_x // ブロックの大きさ)

        # 動かせるブロックの座標の範囲  行(0~10) 列(0~20)
        if self.point_move_block['W'] < 0:
            self.point_move_block['W'] = 0
        if self.point_move_block['W'] >= 10:
            self.point_move_block['W'] = 9

        if self.point_move_block['H'] < 0:
            self.point_move_block['H'] = 0
        if self.point_move_block['H'] >= 20:
            self.point_move_block['H'] = 19

        # 時間が経ったらタイマーの数を減らす。
        if pyxel.frame_count % DEFAULT_FPS == 0:
            self.count_down_timer()

        # マウス左クリックで 右回転()
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.count_right_mouth_click += 1
        # マウス右クリックで ブロック固定()
        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            self.fix_block()

        # キーボードのQボタンでGIVEUP
        if pyxel.btnp(pyxel.KEY_Q):
            self.timeup = True

    def update_timeup_mode(self):
        # リセットと終了だけ受け付ける
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.game_init()

        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)  # 一回きれいさっぱりに

        if self.timeup is True:
            self.draw_timeup_mode()
            return

        # スコアの表示
        pyxel.text(85, 10, "HIGH SCORE:{}".format(self.high_score), 7)
        pyxel.text(85, 20, "     SCORE:{}".format(self.my_score), 7)
        pyxel.text(85, 30, "TIME:{}:{:0=2}".format(self.timer[0], self.timer[1]), 7)

        pyxel.text(85, 50, "SPIN:", 7)
        pyxel.blt(115, 49, IMAGE_ID0, 40, 0, BLOCK_WH * 2, BLOCK_WH * 2)
        pyxel.text(85, 70, " FIX:", 7)
        pyxel.blt(115, 69, IMAGE_ID0, 56, 0, BLOCK_WH * 2, BLOCK_WH * 2)
        pyxel.text(85, 100, "GIVEUP: Q key", 7)

        # ステージを描画する。
        for itt_h, stage_row in enumerate(self.stage):
            for itt_w, stage_cell in enumerate(stage_row):
                pyxel.blt(itt_w * BLOCK_WH, itt_h * BLOCK_WH, IMAGE_ID0,
                          IMAGE_POINTS.get(stage_cell).get('W'), IMAGE_POINTS.get(stage_cell).get('H'),
                          BLOCK_WH, BLOCK_WH, 10)

        # 動かしているブロックを描画する
        vector = self.block_vector.get(self.count_right_mouth_click % 4)
        pyxel.bltm(self.point_move_block.get('W') * BLOCK_WH, self.point_move_block.get('H') * BLOCK_WH, IMAGE_ID0,
                   IMAGE_POINTS.get(self.my_block).get('W') + vector.get('W'), IMAGE_POINTS.get(self.my_block).get('H') + vector.get('H'),
                   MAP_TIP_WH, MAP_TIP_WH, 10)  # 10は透明色の設定。10(黄色)を画像の透明色に設定している

    def draw_timeup_mode(self):
        # 用意した画像を表示
        pyxel.bltm(0, 0, IMAGE_ID1,
                   0, 0,
                   16, 16, 10)
        if self.my_score > self.high_score:
            pyxel.text(40, 100, "NEW RECORD!!", pyxel.frame_count % 16)
        else:
            pyxel.text(40, 100, "NICE GAME !!", 7)

        pyxel.text(40, 110, "SCORE:{}".format(self.my_score), 7)
        pyxel.text(20, 140, "RETRY:MOUSE_LEFT_BUTTON", 7)
        pyxel.text(20, 150, "QUIT:MOUSE_RIGHT_BUTTON", 7)

    def fix_block(self):
        # ブロック固定する
        # ブロックの行列と、ステージの行列を比較する。変数名つけるのとか彷徨ってる
        block_dict = {
            'Z': blockarr.ARR_Z,
            'T': blockarr.ARR_T,
            'O': blockarr.ARR_O,
            'S': blockarr.ARR_S,
            'L': blockarr.ARR_L,
            'I': blockarr.ARR_I,
            'J': blockarr.ARR_J,
        }

        # 固定して大丈夫か確認
        for check_H in range(MAP_TIP_WH):
            for check_W in range(MAP_TIP_WH):
                # 固定しようとしてすでに何かある場合は処理を終わらせる
                if block_dict[self.my_block][self.count_right_mouth_click % 4][check_H][check_W] != 'EMP' and self.stage[self.point_move_block.get('H') + check_H][self.point_move_block.get('W') + check_W] != 'EMP':
                    # 効果音を鳴らす
                    pyxel.play(0, 5)
                    return
        # ブロックを固定させる
        for fix_H in range(MAP_TIP_WH):
            for fix_W in range(MAP_TIP_WH):
                if self.stage[self.point_move_block.get('H') + fix_H][self.point_move_block.get('W') + fix_W] != 'EMP':
                    continue
                self.stage[self.point_move_block.get('H') + fix_H][self.point_move_block.get('W') + fix_W] = block_dict[self.my_block][self.count_right_mouth_click % 4][fix_H][fix_W]
        pyxel.play(0, 6)
        # 一列そろったかチェック
        self.line_check()

        # クリック数をリセット
        self.count_right_mouth_click = 0

        # ブロックを変更する。
        self.my_block = choice(['Z', 'T', 'O', 'S', 'L', 'I', 'J'])

    def line_check(self):
        # 一列そろったら消す処理: col.pop(n-1段目) col.insert(n-1段目, 空の段)
        line_count = 0
        for itt, line in enumerate(self.stage):
            if line[0] == 'NONE':  # 始めの列がNONE = ゲーム外領域なので処理終了
                break
            if 'EMP' not in line:
                line_count += 1
                self.stage.pop(itt)
                self.stage.insert(0, deepcopy(ENPTY_ROW))
        self.score_add(line_count)

    def score_add(self, line_count):
        if line_count == 0:
            return
        self.my_score += 100 * (2 ** (line_count - 1))
        print('my_score:', self.my_score)
        pyxel.play(0, 7)

    def count_down_timer(self):
        # タイマーを減らす
        if self.timer[0] + self.timer[1] == 0:
            self.timeup = True
            pass
        self.timer[1] -= 1
        if self.timer[1] < 0:
            self.timer[0] -= 1
            self.timer[1] = 59

    def high_score_check(self):
        if self.my_score > self.high_score:
            self.high_score = self.my_score


App()
