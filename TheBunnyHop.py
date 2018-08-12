# Author Carlouie
# Created August 10, 2018
# Updated August 11, 2018

import pygame
import time
import random

pygame.init()

#CONSTANT VARIABLES

#ENVIRONMENT
display_width = 800
display_height = 600

black = (0,0,0)
brown = (255, 248, 220)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
darkgreen = (34,139,34)

#GAME VARIABLES
bunny_width = 55

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('THE BUNNY HOP')
clock = pygame.time.Clock()

#CHARACTERS

#player
bunnyImg = pygame.image.load('bunnyImg.jfif')
bunnyImg = pygame.transform.scale(bunnyImg, (50,75))

#potholes

#hunters

#bush


#GAME ITEMS

def potholes_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("DODGED: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def potholes(holex, holey, holew, holeh, color):
    pygame.draw.rect(gameDisplay, color, [holex, holey, holew, holeh])
    
def grasses(grassx, grassy, grassw, grassh, color):
    pygame.draw.rect(gameDisplay, color, [grassx, grassy, grassw, grassh])   

def bunny(x,y):
    gameDisplay.blit(bunnyImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    game_loop()

def fell():
    message_display('YOU FELL IN A HOLE!')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0

#STARTING BLOCK
    #potholes
    hole_startx = random.randrange(0, display_width)
    hole_starty = -300
    hole_speed = 3
    hole_width = 75
    hole_height = 75

    #grass
    grass_startx = random.randrange(0, display_width)
    grass_starty = -700
    grass_speed = 7
    grass_width = 75
    grass_height = 75

    #number of blocks dodged
    dodged = 0


    gameExit = False

#EVENT HANDLING

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change
        gameDisplay.fill(green)

        #GRASS BLOCKS (Movement)
        #grass
        grasses(grass_startx, grass_starty, grass_width, grass_height, darkgreen)
        grass_starty += grass_speed
    
        
        #POTHOLES
        potholes(hole_startx, hole_starty, hole_width, hole_height, brown)    
        hole_starty += hole_speed

        #BUNNY
        bunny (x,y)
        potholes_dodged(dodged)

#EVENT LOGIC STATEMENT

        #WALLS
        if x>display_width - bunny_width or x < -1:
            fell()

        #GRASSES
        #grass
        if grass_starty>display_height:
            grass_starty = 0 - grass_height
            grass_startx = random.randrange(0, display_width)
    
        #POTHOLES
        if hole_starty> display_height:
            hole_starty = 0 - hole_height
            hole_startx = random.randrange(0, display_width)
            dodged +=1
            hole_speed += .5
            

        #FALLING IN THE POTHOLES
        if y <hole_starty+hole_height:
            print('y crossover')

            if x > hole_startx and x < hole_startx + hole_width or x+bunny_width > hole_startx and x + bunny_width < hole_startx+hole_width:
                print('x crossover')
                fell()


        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
        

