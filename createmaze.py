import random, savehelper, pygame
from savehelper import *
complete = True

def createmaze():
    complete = False
    playerx = int(loadvar("playerx"))
    playery = int(loadvar("playery"))
    flagx = int(loadvar("flagx"))
    flagy = int(loadvar("flagy"))
    score = int(loadvar("score"))
    bombs = loadstring("bombs")
    complete =bool(loadvar("complete"))
    numberofbombs = round(score/100)+1
    flagx = random.randint(0,750)
    flagy = random.randint(0,550)
    bombs = []
    for lmao in range(numberofbombs):
        tempbombx = random.randint(0, 750)
        tempbomby = random.randint(0, 550)
        tempbomb = pygame.Rect(tempbombx, tempbomby, 50, 50)
        while flag.colliderect(bomb1) or player.colliderect(bomb1):
            tempbombx = random.randint(0, 750)
            tempbomby = random.randint(0, 550)
            tempbomb1 = pygame.Rect(tempbombx, tempbomby, 50, 50)
        bomb = [tempbombx,tempbomby]
        bombs.append(bomb)
        print(bombs)
    flag = pygame.Rect(flagx, flagy, 50, 50)
    player=pygame.Rect(playery,playerx,50,50)
    print("one point gained")
    save(playerx,"playerx")
    save(playery,"playery")
    save(flagx,"flagx")
    save(flagy,"flagy")
    save(bombs, "bombs")
    save(score, "score")
    save(complete,"complete")
    saveall()
