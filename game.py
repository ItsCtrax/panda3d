from direct.showbase.ShowBase import ShowBase

from hero import Hero
from mapmanager import Mapmanager


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand(8)  # Завантажити два шари: layers0 та layers1
        self.hero = Hero((10, 10, 2), self.land)  # Позиція героя
        base.camLens.setFov(90)


game = Game()
game.run()
