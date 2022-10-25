from pygame.sprite import Sprite
from pygame.image import load
from pygame import Surface, mouse, transform
import math
import pyganim

import os
import random

WHITE = (255, 255, 255)
COLOR = "#888888"
WIN_WIDTH = 680
WIN_HEIGHT = 480
GREY=(190,190,190)

ANIMATION_SWORD=['images/Bullet/sword.png',
                'images/Bullet/sword1.png',
                'images/Bullet/sword2.png']
ANIMATION_DELAY=0.1



class Attack(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        # self.pos = (x, y)
        self.life=5
        #self.speed = 0
        #self.speedx = self.speed * self.dir[0]
        #self.speedy = self.speed * self.dir[1]
        #print('angle',angle)

        self.image = Surface((50 ,40))
        #self.image.fill(COLOR)
        #self.image = bullet_img
        #self.image = transform.scale(ANIMATION_SWORD, (90, 90))
        #self.image.set_colorkey(WHITE)
        #self.image = transform.rotate(self.image, angle)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        def make_boltAnim(anim_list, delay):
           boltAnim = []
           for anim in anim_list:
               boltAnim.append((anim, delay))
           Anim = pyganim.PygAnimation(boltAnim)
           return Anim


        self.boltAnimAttack = make_boltAnim(ANIMATION_SWORD, ANIMATION_DELAY)
        self.boltAnimAttack.play()

    def update(self):
        self.image.fill(GREY)
        self.image.set_colorkey('grey')
        #self.boltAnimAttack.blit(self.image, (0, 0))
        #self.rect.x += self.speedx
        #self.rect.y += self.speedy

        self.life-=1
        if self.life<1:
        #if self.rect.bottom < 0 or self.rect.right < 0 or self.rect.top > WIN_HEIGHT or self.rect.left > WIN_WIDTH:
             self.kill()

         #   print('kill')

    def draw(self, surf):
        sword_rect = self.rect.get_rect(bottom=(self.rect.x, self.rect.y))
        surf.blit(self.rect, sword_rect)
        #print('blit')
