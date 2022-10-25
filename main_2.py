# -*- coding:utf-8 -*-

import pygame
import random
import pyganim
from Player import Player
from Goblin import Goblin
from mob import Mob
from pygame.sprite import Sprite
from Platforms import Platform
from Platforms import Other
from Platforms import Others
from Platforms import Otherss
from Platforms import Othersss
from Platforms import Otherssss
from Attack import Attack
import time
from pygame.image import load

#from pygame import FreeType     
from time import sleep

WIN_WIDTH = 1334
WIN_HEIGHT =750
SIZE = (WIN_WIDTH, WIN_HEIGHT)

WHITE=(255,255,255)
clock=pygame.time.Clock()
colw=50
colh=50
colx=600
coly=480
ANIMATION_HURT = ['images/hero/herohurt.png',           
                'images/hero/herohurt1.png']
fon=pygame.image.load('images/fon.png')
ANIMATION_BOSS=['images/boss/boss1',
                'images/boss/boss2',
                'images/boss/boss3',
                'images/boss/boss4']


# создаем окно
window = pygame.display.set_mode(SIZE)
# создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

COLOR=(10,120,10)
mana=233
ANIMATION_DELAY = 0.2
mobgf_img=load('images/mob/boss55.png')
icons_img=load('images/hero/icons.png')
hp_img=load('images/hero/hp.png')
mana_img=load('images/hero/mana.png')
boss_img=load('images/hero/boss.png')
flag_img=load('images/hero/flag.png')
mobd=random.randrange(3,45)

herox=55
heroy=300
#goblinx=100
#gobliny=300

# создаем героя

#goblin=Goblin(goblinx,gobliny)
left = right = up =  down = dead=False
attack=False
Boss=True
# создание уровня
level = [
    '----------------------------------',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                                -',
    '-                              **-',
    '-                        **      -',
    '-               **               -',
    '-       **                       -',
    '-**                              -',
    '-                                -',
    '-                                -',
    '-                                -',
    '----------------------------------']
entities = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()
goblin=Goblin()
hero = Player(herox, heroy)
sprite_group.add(hero)
entities.add(goblin)
platfroms = []
mobs = pygame.sprite.Group()
#enemy= pygame.sprite.Group()
bullets = pygame.sprite.Group()
attacks = pygame.sprite.Group()
for i in range(30):
    #print(mobd)
    m = Mob()
    entities.add(m)
    mobs.add(m)
x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            pl = Platform(x, y)
            sprite_group.add(pl)
            platfroms.append(pl)

        x += 40
    y += 40
    x = 0

x = 0
y = 0
for row in level:
    for col in row:
        if col == '*':
            ot = Other(x, y)
            sprite_group.add(ot)
            platfroms.append(ot)

        x += 40
    y += 40
    x = 0

x = 0
y = 0
for row in level:
    for col in row:
        if col == '+':
            oto = Others(x, y)
            sprite_group.add(oto)
            platfroms.append(oto)

        x += 40
    y += 40
    x = 0

x = 0
y = 0

x = 0
y = 0
for row in level:
    for col in row:
        if col == '/':
            sss = Otherss(x, y)
            sprite_group.add(sss)
            platfroms.append(sss)

        x += 40
    y += 40
    x = 0

x = 0
y = 0

for row in level:
    for col in row:
        if col == '&':
            res = Othersss(x, y)
            sprite_group.add(res)
            platfroms.append(res)

        x += 40
    y += 40
    x = 0

x = 0
y = 0
for row in level:
    for col in row:
        if col == '.':
            resd = Otherssss(x, y)
            sprite_group.add(resd)
            platfroms.append(resd)

        x += 40
    y += 40
    x = 0

x = 0
y = 0
pygame.font.init()
score=0 # очки
hearts=240
coins=5
SPACE=False
mobdam=0
#print(hearts)# сердечки
# открываем игровой цикл




#E1 = Enemy()
running = True
timer = pygame.time.Clock()

while running:
    # блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False


        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True
            if e.key == pygame.K_DOWN:
                down = True

        if e.type == pygame.MOUSEBUTTONDOWN:
            #if e.key==pygame.K_SPACE:
                if mana>=30:
                    mana-=30
                    attack=True
                SPACE=True
                s = Attack(hero.rect.x, hero.rect.y+20)
                entities.add(s)  # добавить в список спрайтов пулю
                bullets.add(s)# добавить в список пуль пулю

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False
            if e.key == pygame.K_DOWN:
                down = False
        if e.type == pygame.MOUSEBUTTONUP:
            #if e.key==pygame.K_SPACE:
                #mana-=30
                attack=False
                SPACE=False
                s = Attack(hero.rect.x, hero.rect.y + 20)
                entities.add(s)  # добавить в список спрайтов пулю(xd,])
                bullets.add(s)  # добавить в список пуль пулю
    #E1.update()


    # закрашиваем рабочую поверхность
    #screen.fill('grey')
    #screen.blit(icons_img, (510, 50))
    screen.blit(fon,(0,0))
    screen.blit(icons_img, (40, 40))
    screen.blit(mana_img, (40, 110))
    screen.blit(hp_img, (40, 80))
    screen.blit(flag_img, (40, 150))
    #screen.blit(boss_img, (500, 391))


    #E1.draw(screen)
    if SPACE:#если нажат пробел создаем экземпляр объекта меч
        s = Attack(hero.rect.x, hero.rect.y+20)
        entities.add(s)  # добавить в список спрайтов пулю
        bullets.add(s)  # добавить в список пуль пулю
    # отображение героя
    hero.update(left, right, up, platfroms,attack,dead)
    #goblin.update(left, right, up, platfroms, attack, dead)
    entities.update()  # вычисление новых координат всех объектов
    #sprite_group.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #for hit in hits:
        #score+=random.randint(1,3)
        #hearts+=random.randint(1,3)
        #coins+=random.randint(3,7)
       #m = Mob()
        #entities.add(m)
        #mobs.add(m)
    #earts=240
    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(hero, mobs, False)
    if hits:
        hearts-=0
        mobdam=0
        #print(hearts)
    if hearts<=0:
        dead =True
        #running = False


    entities.draw(screen)
    sprite_group.draw(screen)



    window.blit(screen, (0, 0))
    #screen.blit(icons_img, (510, 50))



# обновляем окно
    f1 = pygame.font.SysFont('arial', 35)
    #text1 = f1.render('Очки', 1, (0, 0, 0))
    #text2 = f1.render(str(score), 1, (0, 0, 0))
    #text3 = f1.render('', 1, (0, 0, 0))
    text4 = f1.render(str(hearts), 1, (255, 255, 255))
    text5 = f1.render('Knight', 1, (255, 255, 255))
    text6 = f1.render(str(mana), 1, (255, 255, 255))
    #text7 = f1.render('Knight', 1, (0, 0, 0))
    #text5 = f1.render(str(mobd), 1, (0, 0, 0))
    #text6 = f1.render('кол-во мобов', 1, (0, 0, 0))
    #text8 = f1.render(str(mobdam), 1, (0, 0, 0))
    #text9 = f1.render('монетки', 1, (0, 0, 0))
    #text10 = f1.render(str(coins), 1, (0, 0, 0))
    #window.blit(text1, (510, 50))
    #window.blit(text2, (610, 50))
    #window.blit(text3, (50, 100))
    window.blit(text4, (80, 75))
    window.blit(text5, (80, 40))
    window.blit(text6, (80, 110))
    #window.blit(text5, (610, 150))
    #window.blit(text6, (510, 150))
    #window.blit(text7, (510, 200))
    #window.blit(text8, (610, 200))
    #window.blit(text9, (510, 250))
    #window.blit(text10, (610, 250))
    pygame.display.flip()
    timer.tick(45)