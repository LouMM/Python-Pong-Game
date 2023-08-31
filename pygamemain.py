import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up paddles
paddle_width = 15
paddle_height = 80

paddle1_x = 50
paddle1_y = window_height // 2 - paddle_height // 2
paddle1_speed = 0

paddle2_x = window_width - 50 - paddle_width
paddle2_y = window_height // 2 - paddle_height // 2
paddle2_speed = 0

paddle_speed = 5

# Set up ball
ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_speed_x = 3
ball_speed_y = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                paddle1_speed = -paddle_speed
            elif event.key == K_s:
                paddle1_speed = paddle_speed
            elif event.key == K_UP:
                paddle2_speed = -paddle_speed
            elif event.key == K_DOWN:
                paddle2_speed = paddle_speed
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                paddle1_speed = 0
            elif event.key == K_UP or event.key == K_DOWN:
                paddle2_speed = 0

    # Update paddles' positions
    paddle1_y += paddle1_speed
    paddle2_y += paddle2_speed

    # Keep paddles within the screen
    paddle1_y = max(0, min(paddle1_y, window_height - paddle_height))
    paddle2_y = max(0, min(paddle2_y, window_height - paddle_height))

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    elif ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Bounce the ball off the walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, Rect(paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, Rect(paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()