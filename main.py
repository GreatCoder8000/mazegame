import pygame, time, savehelper,createmaze
from savehelper import *

pygame.init()

#vars
size = (800,600)
screen = pygame.display.set_mode(size)
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
turtle = pygame.image.load('turtle.png').convert_alpha()
bomb = pygame.image.load('bomb.png').convert_alpha()

screen.fill(WHITE)
pygame.display.update()
time.sleep(1)

import titlescreen

done = False
w = False
a = False
s = False
d = False
createmaze.createmaze()
comp = False
streak = 1
saving = 0
while not done:
    if comp == True:
        createmaze.createmaze()
        comp = False
    screen.fill(WHITE)
    #start of loop
    playerx = int(loadvar("playerx"))
    playery = int(loadvar("playery"))
    flagx = int(loadvar("flagx"))
    flagy = int(loadvar("flagy"))
    score = int(loadvar("score"))
    bomb1x = int(loadvar("bomb1x"))
    bomb1y = int(loadvar("bomb1y"))
    bomb2x = int(loadvar("bomb2x"))
    bomb2y = int(loadvar("bomb2y"))
    scoret = mediumfont.render("score = "+str(score)+" streak = "+str(streak), False, (255, 0, 0))
    scorebox = pygame.Rect(50, 50, 50, 50)
    screen.blit(scoret,scorebox)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w = True
            if event.key == pygame.K_a:
                a = True
            if event.key == pygame.K_s:
                s = True
            if event.key == pygame.K_d:
                d = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w = False
            if event.key == pygame.K_a:
                a = False
            if event.key == pygame.K_s:
                s = False
            if event.key == pygame.K_d:
                d = False
    if w == True:
        playerx-=10
    if a == True:
        playery-=10
    if s == True:
        playerx+=10
    if d == True:
        playery+=10
    if playerx <= 0:
        playerx =0
    if playerx >= 600:
        playerx =600
    if playery <= 0:
        playery =0
    if playery >= 800:
        playery = 800
    player=pygame.Rect(playery,playerx,50,50)
    flag=pygame.Rect(flagx,flagy,50,50)
    bomb1 = pygame.Rect(bomb1x, bomb1y, 50, 50)
    bomb2 = pygame.Rect(bomb2x, bomb2y, 50, 50)
    screen.blit(flagimage,flag)
    screen.blit(turtle,player)
    screen.blit(bomb,bomb1)
    screen.blit(bomb, bomb2)
    if player.colliderect(flag):
        score+=streak
        streak+=1
        print("collided")
        comp = True
    if player.colliderect(bomb1):
        score-=5
        print("collided")
        comp = True
        streak = 1
    if player.colliderect(bomb2):
        score-=5
        print("collided")
        comp = True
        streak = 1
    #end of loop
    saving +=1
    if saving >= 60:
        print("saving")
        save(score, "score")
        save(playerx,"playerx")
        save(playery,"playery")
        save(flagx,"flagx")
        save(flagy,"flagy")
        saveall()
        save = 0
    pygame.display.update()
    clock.tick(60)

