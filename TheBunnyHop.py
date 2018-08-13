# Author Carlouie/Stephen
# Created August 10, 2018
# Updated August 11, 2018

#8/12 CARLOUIE: start menu, cliff on the side
#8/12 STEPHEN: bunny, pothole circle, sound effects

import pygame
import time
import random

pygame.init()

#CONSTANT VARIABLES

#ENVIRONMENT
display_width = 800
display_height = 600

black = (0,0,0)
brown = (109, 99, 72)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
darkgreen = (34,139,34)
bright_red = (255,0,0)
bright_green = (0,255,0)

#GAME VARIABLES
bunny_width = 55

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('THE BUNNY HOP')
clock = pygame.time.Clock()

#CHARACTERS

#player
bunnyImg = pygame.image.load('bunnyImg.jfif')
bunnyImg = pygame.transform.scale(bunnyImg, (50,75))

#background
bgImg = pygame.image.load('backImg.png')
bgImg = pygame.transform.scale(bgImg, (800,600))

#carrots
carrotImg = pygame.image.load('carrotImg.png')
carrotImg = pygame.transform.scale(carrotImg,(35,35))

#blackhole
blackholeImg = pygame.image.load('blackholeImg.png')

#GAME ITEMS

def potholes_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("DODGED: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def blackholes(blholex, blholey, blholew, blholeh):
    gameDisplay.blit(blackholeImg,[blholex, blholey, blholew, blholeh])

def potholes(holex, holey, holew, holeh, color):
    pygame.draw.rect(gameDisplay, color, [holex, holey, holew, holeh])
    
def grasses(grassx, grassy, grassw, grassh, color):
    pygame.draw.rect(gameDisplay, color, [grassx, grassy, grassw, grassh])   

def carrots (carx, cary):
    gameDisplay.blit(carrotImg, [carx,cary])
                     
def bunny(x,y):
    gameDisplay.blit(bunnyImg,(x,y))

def bg():
    gameDisplay.blit(bgImg,(0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
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

def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()#grabs mouse
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+50 > mouse[1] > y: #if x coordinate + 100(width)
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h)) #displays butons
        if click[0] ==1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("THE BUNNY HOP", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("HOP!", 150,450,100,50, green, bright_green,"play")
        button("QUIT!", 550,450,100,50, red, bright_red, "quit")


        #pygame.draw.rect(gameDisplay, red, (550,450,100,50)) #display buttons

           
        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0

#STARTING BLOCK
    #blackholes
    blhole_startx = random.randrange(0, display_width)
    blhole_starty = -300
    blhole_speed = 3
    blhole_width = 75
    blhole_height = 75
  
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

    #carrots
    car_startx = random.randrange(0, display_width)
    car_starty = -1500
    car_speed = 15
   
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
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change
        bg()
        
#GRASS BLOCKS (Movement)
        #GRASS
        grasses(grass_startx, grass_starty, grass_width, grass_height, darkgreen)
        grass_starty += grass_speed

        #BLACKHOLE
        blackholes(blhole_startx, blhole_starty, blhole_width, blhole_height)
        blhole_starty += blhole_speed
        
        #POTHOLES
        potholes(hole_startx, hole_starty, hole_width, hole_height, brown)    
        hole_starty += hole_speed

        #BUNNY
        bunny (x,y)
        potholes_dodged(dodged)

        #CARROTS
        carrots (car_startx, car_starty)
        car_starty += car_speed
#EVENT LOGIC STATEMENT

        #WALLS
        if x>display_width - bunny_width or x < -1:
            fell()

        #GRASSES
        #grass
        if grass_starty>display_height:
            grass_starty = 0 - grass_height
            grass_startx = random.randrange(0, display_width)

        #BLACKHOLE
        if blhole_starty>display_height:
            blhole_starty = 0 - blhole_height
            blhole_startx = random.randrange(0, display_width)
            dodged +=1
            blhole_speed =+ .5
    
        #POTHOLES
        if hole_starty> display_height:
            hole_starty = 0 - hole_height
            hole_startx = random.randrange(0, display_width)
            dodged +=1
            hole_speed += .5

        #CARROTS
        if car_starty>display_height:
            car_starty = -1500
            car_startx = random.randrange(0, display_width)
           

        #FALLING IN THE POTHOLES
        if y <hole_starty+hole_height:
            print('y crossover')
            
            if x > hole_startx and x < hole_startx + hole_width or x+bunny_width > hole_startx and x + bunny_width < hole_startx+hole_width:
                print('x crossover')
                fell()

        if y <blhole_starty+blhole_height:
            print('y crossover')
            
            if x > blhole_startx and x < blhole_startx + blhole_width or x + bunny_width > blhole_startx and x + bunny_width < blhole_startx + blhole_width:
                print('x crossover')
                fell()
        
        pygame.display.update()
        clock.tick(60)
        
game_intro()
game_loop()
pygame.quit()
quit()
        

