import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sumesh Game")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Set up player
player_size = 50
player_x, player_y = width // 2 - player_size // 2, height - player_size - 10
player_speed = 10
 
# Set up bullets
bullet_size = 10
bullet_speed = 5
bullets = []

# Set up enemies
enemy_size = 50
enemy_speed = 3
enemies = []

def create_enemy():
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    return {'x': enemy_x, 'y': enemy_y}

# Main game loop
clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append({'x': player_x + player_size // 2 - bullet_size // 2, 'y': player_y})

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet['y'] -= bullet_speed
        if bullet['y'] < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy['y'] += enemy_speed
        if enemy['y'] > height:
            enemies.remove(enemy) 

    # Check for collisions between bullets and enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (
                enemy['x'] < bullet['x'] < enemy['x'] + enemy_size and
                enemy['y'] < bullet['y'] < enemy['y'] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Generate enemies
    if random.randint(1, 50) == 1:
        enemies.append(create_enemy())

    # Check for collisions between player and enemies
    for enemy in enemies:
        if (
            player_x < enemy['x'] < player_x + player_size and
            player_y < enemy['y'] < player_y + player_size
        ):
            running = False

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))
    for bullet in bullets:
        pygame.draw.rect(screen, red, (bullet['x'], bullet['y'], bullet_size, bullet_size))
    for enemy in enemies:
        pygame.draw.rect(screen, red, (enemy['x'], enemy['y'], enemy_size, enemy_size))

    # Draw score
    score_text = font.render(f"Score: {score}", True, red)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()   
 