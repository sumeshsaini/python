import pygame
import sys
display=pygame.display.set_mode((1000,600))
image=pygame.image.load("C:/Users/Sumesh Saini/Desktop/Untitled.png")
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.blit(image,(0,0))
    pygame.display.update()
    display.fill((0,0,0))
