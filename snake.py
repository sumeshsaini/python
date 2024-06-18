 
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (1, 0)  # Initial direction (right)
snake_speed = 20
snake_timer = pygame.time.Clock()

# Set up food
food = (random.randrange(1, (width//cell_size)) * cell_size,
        random.randrange(1, (height//cell_size)) * cell_size)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    head = (snake[0][0] + snake_direction[0] * cell_size,
            snake[0][1] + snake_direction[1] * cell_size)
    snake = [head] + snake[:-1]

    # Check for collisions with the walls
    if (
        head[0] < 0 or head[0] >= width or
        head[1] < 0 or head[1] >= height
    ):
        running = False

    # Check for collisions with itself
    if head in snake[1:]:
        running = False

    # Check for collisions with food
    if head == food:
        snake.append(snake[-1])  # Grow the snake
        food = (random.randrange(1, (width//cell_size)) * cell_size,
                random.randrange(1, (height//cell_size)) * cell_size)

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    snake_timer.tick(snake_speed)

# Quit Pygame
pygame.quit()
sys.exit()
