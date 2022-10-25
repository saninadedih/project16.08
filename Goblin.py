import pygame
GREEN=(56,45,32)

WIN_WIDTH = 1334
WIN_HEIGHT =750
class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,35))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.center=(WIN_WIDTH/2,WIN_HEIGHT/2)
    def update(self):
        self.rect.x+=10
        if self.rect.left>WIN_WIDTH:
            self.rect.right=0