import pygame, time, savehelper,createmaze,sys, math
from savehelper import *
#nice
pygame.init()

#vars
size = (800,600)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
smallfont = pygame.font.SysFont('Comic Sans MS', 20)
mediumfont = pygame.font.SysFont('Comic Sans MS', 30)
bigfont = pygame.font.SysFont('Comic Sans MS', 45)
clock = pygame.time.Clock()


#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()

flagimage = pygame.image.load('flags.png').convert_alpha()
playerimagebig = pygame.image.load('banana.jpeg')
bombimage = pygame.image.load('bomb.png').convert_alpha()

bombimage = pygame.transform.scale(bombimage, (30, 30))
playerimage = pygame.transform.scale(playerimagebig, (50, 50))

screen.fill(WHITE)
pygame.display.update()
time.sleep(1)

import titlescreen

done = False
addstreak = True
w = False
a = False
s = False
d = False
createmaze.createmaze(size)
comp = False
streak = int(loadvar("streak"))
playerx = int(loadvar("playerx"))
playery = int(loadvar("playery"))
flagx = int(loadvar("flagx"))
flagy = int(loadvar("flagy"))
score = int(loadvar("score"))
bombs = loadlist("bombs")
while not done:
    if comp == True:
        save(streak,"streak")
        save(playerx,"playerx")
        save(playery,"playery")
        save(flagx,"flagx")
        save(flagy,"flagy")
        save(bombs, "bombs")
        save(score, "score")
        saveall()
        createmaze.createmaze(size)
        comp = False
        playerx = int(loadvar("playerx"))
        playery = int(loadvar("playery"))
        flagx = int(loadvar("flagx"))
        flagy = int(loadvar("flagy"))
        score = int(loadvar("score"))
        bombs = loadlist("bombs")
        streak = int(loadvar("streak"))
    screen.fill(WHITE)
    #start of loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            size = (event.w,event.h)
            screen = pygame.display.set_mode(size,
                                              pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                w = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                a = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                s = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                d = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                w = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                a = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                s = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                d = False
    if w == True:
        playerx-=5
    if a == True:
        playery-=5
    if s == True:
        playerx+=5
    if d == True:
        playery+=5
    if playerx <= 0:
        playerx =0
    if playerx >= size[1]:
        playerx = size[1]
    if playery <= 0:
        playery =0
    if playery >= size[0]:
        playery = size[0]
    player=pygame.Rect(playery,playerx,50,50)
    flag=pygame.Rect(flagx,flagy,50,50)
    numberofbombs = round(score / 50) + 1
    if score <= 0:
        numberofbombs = 0
    if numberofbombs == 1:
        bombx = int(bombs[0])
        bomby = int(bombs[1])
        bomb = pygame.Rect(bombx, bomby, 30, 30)
        screen.blit(bombimage, bomb)
        if player.colliderect(bomb):
            score -= 20
            comp = True
            streak = 1
    else:
        for b in range(numberofbombs):
            bombx = int(bombs[(b+1)*2-2])
            bomby = int(bombs[(b+1)*2-1])
            bomb = pygame.Rect(bombx, bomby, 50, 50)
            screen.blit(bombimage, bomb)
            if player.colliderect(bomb):
                score -= 20
                comp = True
                streak = 1
    screen.blit(flagimage,flag)
    screen.blit(playerimage,player)
    scoret = mediumfont.render("score = " + str(score) + " streak = " + str(streak), False, (255, 0, 0))
    scorebox = pygame.Rect(50, 50, 50, 50)
    screen.blit(scoret, scorebox)
    if player.colliderect(flag):
        score+=streak
        streak*=1.1
        streak = math.ceil(streak)
        addstreak = True
        comp = True
    #end of loop
    pygame.display.update()
    clock.tick(180)

