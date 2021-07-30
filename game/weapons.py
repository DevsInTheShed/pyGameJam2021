class Weapon:
    def __init__(self, ammo, cooldown, damage, img=None, ammoImg=None):
        self.active = False
        self.cooldown = cooldown
        self.timer = 0
        self.bullet_count = ammo
        self.maxAmmo = self.bullet_count
        self.damage = damage
        self.image = img
        self.ammoImg = ammoImg

    def decr(self):
        if not self.bullet_count == -1:
            self.bullet_count -= 1