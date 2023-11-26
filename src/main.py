# Raymond DANG
# 26/11/2023

import pygame

WIDTH = 900
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((900, 720))
screenProp = pygame.time.Clock()
playerPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)
pygame.display.set_caption("tristan stinks")
imagePath = "C:/Users/Ray/Code/snake/resources/images/background-1.png"
imageLoad = pygame.image.load(imagePath)
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, 'red', playerPosition, 40)


    # flip() the display to put your work on screen
    pygame.display.flip()

    screenProp.tick(144)  # limits FPS to 60
    
pygame.quit()