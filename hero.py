key_switch_camera = "c"
key_switch_mode = "z"

key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
key_up = "e"
key_down = "q"

key_turn_left = "n"
key_turn_right = "m"

def check_dir(self, angle):
    if angle >= 0 and angle <= 20:
        return (0, -1)
    elif angle <= 65:
        return (1, -1)
    elif angle <= 110:
        return (1, 0)
    elif angle <= 155:
        return (1, 1)
    elif angle <= 200:
        return (0, 1)
    elif angle <= 245:
        return (-1, 1)
    elif angle <= 290:
        return (-1, 0)
    elif angle <= 335:
        return (-1, -1)
    else:
        return (0, -1)

class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('n', self.turn_left)
        base.accept('n'+'-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m'+'-repeat', self.turn_right)
        base.accept('w', self.move_forward)
        base.accept('s', self.move_back)
        base.accept('a', self.move_left)
        base.accept('d', self.move_right)
        base.accept('e', self.move_up)
        base.accept('q', self.move_down)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def move_forward(self):
        self.just_move(self.hero.getH())

    def move_back(self):
        self.just_move((self.hero.getH() + 180) % 360)

    def move_left(self):
        self.just_move((self.hero.getH() + 90) % 360)

    def move_right(self):
        self.just_move((self.hero.getH() - 90) % 360)

    def move_up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def move_down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def just_move(self, angle):
        direction = check_dir(self, angle)
        self.hero.setPos(self.hero.getX() + direction[0], self.hero.getY() + direction[1], self.hero.getZ())

    def try_move(self, angle):
        # Implement collision detection here if needed
        self.just_move(angle)

    def move_to(self, angle):
        self.try_move(angle)

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
