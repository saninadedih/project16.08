# -*- coding:utf-8 -*-

from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import Platforms
import pyganim
import random
import math
from pygame.image import load

MOVE_SPEED = 7
JUMP_POWER = 10



WHITE=(255,255,255)

GRAVITY = 0.4
COLOR = ("#888888")
GREY=(105,105,105)
boss_img=load('images/hero/boss.png')
ANIMATION_DELAY = 0.1
ANIMATION_DELAY_AT =0.1
ANIMATION_DELAY_IDLE =0.9
ANIMATION_STAY = ['images/hero/hero.png',
                    'images/hero/hero1.png']
                    #'images/hero/hero2.png',
                    #'images/hero/hero3.png'
#'images/hero/hero2.png',
##'images/hero/hero4.png']

ANIMATION_RIGHT =['images/hero/hero_right1.png',
                    'images/hero/hero_right2.png',
                    'images/hero/hero_right3.png',
                    'images/hero/hero_right4.png',
                    'images/hero/hero_right5.png',
                    'images/hero/hero_right6.png',
                    'images/hero/hero_right7.png']
ANIMATION_LEFT =   ['images/hero/hero_left1.png',
                    'images/hero/hero_left2.png',
                    'images/hero/hero_left3.png',
                    'images/hero/hero_left4.png',
                    'images/hero/hero_left5.png',
                    'images/hero/hero_left6.png',
                    'images/hero/hero_left7.png']
ANIMATION_UP =['images/hero/heroup.png']
ANIMATION_BOSS =['images/hero/boss.png',
                'images/hero/boss1.png',
                'images/hero/boss2.png',
                'images/hero/boss3.png']
ANIMATION_SWORD =['images/Bullet/sword1.png',
                'images/Bullet/sword2.png']
ANIMATION_DEAD =['images/hero/herodead1.png']
                #'images/hero/herodead2.png']
#'images/hero/herodead2.png',
#'images/hero/herodead3.png',
#'#images/hero/herodead4.png',
#'images/hero/herodead5.png']
ANIMATION_Attack=['images/hero/hero_at5.png',
                'images/hero/hero_at6.png',
                'images/hero/hero_at7.png',
                'images/hero/hero_at8.png']
                #['images/hero/hero_at1.png',
                #'images/hero/hero_at2.png',
                #'images/hero/hero_at3.png',
                #'images/hero/hero_at4.png']
                #'images/hero/hero_at6.png',
               # 'images/hero/hero_at7.png',
                #'images/hero/hero_at8.png']
                #'images/hero/hero_at9.png']
                #'images/hero/hero_at30.png',
                #'images/hero/hero_at40.png',
                #'images/hero/hero_at50.png',
                #'images/hero/hero_at60.png']



class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((60,67))
        self.image.set_colorkey(WHITE)
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False


        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = make_boltAnim(ANIMATION_STAY,ANIMATION_DELAY_IDLE)
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimUp = make_boltAnim(ANIMATION_UP, ANIMATION_DELAY)
        self.boltAnimUp.play()

        self.boltAnimAttack=make_boltAnim(ANIMATION_Attack, ANIMATION_DELAY_AT)
        self.boltAnimAttack.play()

        self.boltAnimBOSS = make_boltAnim(ANIMATION_BOSS, ANIMATION_DELAY_IDLE)
        self.boltAnimBOSS.play()

        self.boltAnimSword = make_boltAnim(ANIMATION_SWORD, ANIMATION_DELAY)
        self.boltAnimSword.play()

        self.boltAnimdead = make_boltAnim(ANIMATION_DEAD, ANIMATION_DELAY)
        self.boltAnimdead.play()

    def update(self,left, right, up, platforms,attack,dead):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(WHITE)
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(WHITE)
            self.boltAnimRight.blit(self.image, (0, 0))
        if not(left or right):
            self.xvel = 0
            if not up:
                self.image.fill(WHITE)
                self.boltAnimStay.blit(self.image, (0, 0))
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(WHITE)
            self.boltAnimUp.blit(self.image, (0, 0))

        if attack:
            self.image.fill(WHITE)
            #self.boltAnimSword.blit(self.image, (0, 0))
            self.boltAnimAttack.blit(self.image, (0, 0))
        if dead:
            self.image.fill(WHITE)
            self.boltAnimdead.blit(self.image, (0, 0))
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0



