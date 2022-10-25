# -*- coding:utf-8- -*-

from pygame.sprite import Sprite
from pygame.image import load
WHITE=(255,255,255)

class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Other(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Others(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform3.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Otherss(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform6.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Othersss(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform4.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Otherssss(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platforms/platform7.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

