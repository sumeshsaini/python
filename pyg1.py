import pygame
x = pygame.init()
wd = pygame.display.set_mode((500,500))
pygame.display.set_caption("HI This Is My Display")
exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
pygame.quit()
quit()