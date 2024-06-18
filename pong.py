import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up paddles
paddle_width, paddle_height = 20, 100
player1_x, player1_y = 50, height // 2 - paddle_height // 2
player2_x, player2_y = width - 50 - paddle_width, height // 2 - paddle_height // 2
paddle_speed = 5

# Set up ball
ball_size = 20
ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
ball_speed_x, ball_speed_y = 5, 5

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
        player2_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off top and bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y = -ball_speed_y

    # Bounce off paddles
    if (
        player1_x < ball_x < player1_x + paddle_width
        and player1_y < ball_y < player1_y + paddle_height
    ) or (
        player2_x < ball_x < player2_x + paddle_width
        and player2_y < ball_y < player2_y + paddle_height
    ):
        ball_speed_x = -ball_speed_x

    # Check for scoring
    if ball_x < 0 or ball_x > width:
        ball_x = width // 2 - ball_size // 2
        ball_speed_x = -ball_speed_x

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
