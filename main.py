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
bombimage = pygame.image.load('bomb.png').convert_alpha()

screen.fill(WHITE)
pygame.display.update()
time.sleep(1)

import titlescreen

done = False
addstreak = False
w = False
a = False
s = False
d = False
createmaze.createmaze()
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
        createmaze.createmaze()
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
        playerx-=5
    if a == True:
        playery-=5
    if s == True:
        playerx+=5
    if d == True:
        playery+=5
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
    numberofbombs = round(score / 50) + 1
    if score <= 0:
        numberofbombs = 0
    if numberofbombs == 1:
        bombx = int(bombs[0])
        bomby = int(bombs[1])
        bomb = pygame.Rect(bombx, bomby, 50, 50)
        screen.blit(bombimage, bomb)
        if player.colliderect(bomb):
            score -= 20
            print("collided")
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
                print("collided")
                comp = True
                streak = 1
    screen.blit(flagimage,flag)
    screen.blit(turtle,player)
    if player.colliderect(flag):
        score+=streak
        if addstreak == True:
            streak+=1
            addstreak = False
        else:
            streak+=0
            addstreak = True
        print("collided")
        comp = True
    #end of loop
    pygame.display.update()
    clock.tick(180)

