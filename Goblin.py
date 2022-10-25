import pygame
from pygame.image import load
GREEN=(56,45,32)

WIN_WIDTH = 1334
WIN_HEIGHT =750
WHITE=(255,255,255)
class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=load('images/hero/boss2.png')
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.center=(WIN_WIDTH/2,WIN_HEIGHT/2)
    def update(self):
        self.rect.x+=10
        if self.rect.left>WIN_WIDTH:
            self.rect.right=0