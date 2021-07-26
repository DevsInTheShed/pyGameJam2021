class Weapon:
    def __init__(self, ammo, cooldown):
        self.active = False
        self.cooldown = cooldown
        self.timer = 0
        self.bullet_count = ammo

    def decr(self):
        if not self.bullet_count == -1:
            self.bullet_count -= 1