from pygame.sprite import Sprite
from pygame.image import load
import random
import pyganim
from pygame import Surface
import pygame
ANIMATION_BOSS=['images/boss/boss1',
                'images/boss/boss2',
                'images/boss/boss3',
                'images/boss/boss4']
ANIMATION_DELAY = 0.2


WIN_WIDTH = 680
WIN_HEIGHT = 480

COLOR=(10,120,10)
WHITE=(255,255,255)

mob_img=load('images/mob/mobg.png')

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = mob_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIN_HEIGHT - self.rect.height)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        #print('heh')
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > WIN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIN_WIDTH + 20:
            self.image.fill(WHITE)
            self.image.set_colorkey('black')
            self.rect.x = random.randrange(WIN_HEIGHT - self.rect.height)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)
            self.speedx = random.randrange(-3, 3)

    def draw(self, surf):
        #print('hoh')
        mob_rect = self.rect.get_rect(center=(self.rect.x, self.rect.y))
        surf.blit(self.rect, mob_rect)
