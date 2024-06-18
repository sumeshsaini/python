import pygame
import random
pygame.init()

screen_width = 600
screen_height = 400

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#creating a window
game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Cobra X Python")
pygame.display.update()

#game specific vari
exit_game = False
game_over = False
snake_x = 20
snake_y = 20
size = 20
fps = 30
clock = pygame.time.Clock()
velocity_x = 0
velocity_y = 0
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_height)
score = 0


#game loop 
while not exit_game:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0


    snake_x+=velocity_x
    snake_y+=velocity_y
        
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=1
        print(f"Score : {score}")
        food_x = random.randint(0,screen_width)
        food_y = random.randint(0,screen_height)
    game_window.fill(white)
    pygame.draw.rect(game_window,black,(snake_x,snake_y,size,size))
    pygame.draw.rect(game_window,red,(food_x,food_y,size,size))
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()