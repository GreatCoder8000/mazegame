import pygame, time, configparser
from savehelper import *

#vars
size = (800,600)
screen = pygame.display.set_mode(size)
smallfont = pygame.font.SysFont('Comic Sans MS', 20)
mediumfont = pygame.font.SysFont('Comic Sans MS', 30)
bigfont = pygame.font.SysFont('Comic Sans MS', 45)
clock = pygame.time.Clock()

BLUE = ((0,0,255))
BLACK = ((0,0,0))
WHITE = ((255,255,255))

loadimage = pygame.image.load('load.png').convert_alpha()
newimage = pygame.image.load('new.png').convert_alpha()

load = pygame.Rect(300,100,300,200)
new = pygame.Rect(300,350,300,200)
loadt = bigfont.render("Load Game", False, (255,0,0))
newt = bigfont.render("New Game", False, (255,0,0))
screen.blit(loadimage,load)
screen.blit(newimage,new)
pygame.display.update()

done3 = False
while not done3:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if load.collidepoint(mouse_pos):
                choice = "l"
                done3 = True
            if new.collidepoint(mouse_pos):
                choice = "n"
                done3 = True

screen.fill(BLACK)
inputbox = pygame.Rect(300,200,300,50)
pygame.draw.rect(screen, WHITE, inputbox)
if choice == "l":
    message = mediumfont.render("Input game name to load", False, (255,0,0))
elif choice == "n":
    message = mediumfont.render("Input game name to create", False, (255,0,0))
screen.blit(message, inputbox)
pygame.display.update()
done3 = False
active = False
text = ""
while not done3:
    pygame.draw.rect(screen, WHITE, inputbox)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if inputbox.collidepoint(mouse_pos):
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    done3=True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    textt = bigfont.render(text,False,(255,0,0))
    if active == True:
        screen.blit(textt,inputbox)
    elif text == "":
        screen.blit(message,inputbox)
    else:
        screen.blit(textt,inputbox)
    pygame.display.update()
    clock.tick(60)


loadcreatesave(text, choice, {"streak":1, "score":0, "playerx": 0, "playery": 0, "flagx":0, "flagy":0, "bombs":[], "startx":0, "starty":0, "complete":True})

save = config["save"]
