import pygame
pygame.init()

font = pygame.font.SysFont(None, 48)

# Background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Window size
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle and ball
PADDLE_W, PADDLE_H = 15, 100
BALL_SIZE = 20

# Scoreboard
left_score = 0
right_score = 0

left_paddle = pygame.Rect(30, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
right_paddle = pygame.Rect(WIDTH-45, HEIGHT//2 - PADDLE_H//2, PADDLE_W, PADDLE_H)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

ball_speed_x, ball_speed_y = 3, 3
paddle_speed = 8

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y = left_paddle.y - paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y = left_paddle.y + paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y = right_paddle.y - paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y = right_paddle.y + paddle_speed

    # Ball movement
    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    # Ball collision with top/bottom
    if ball.top <= 0:
        ball.top = 0
        ball_speed_y = ball_speed_y * -1
    if ball.bottom >= HEIGHT:
        ball.bottom = HEIGHT
        ball_speed_y = ball_speed_y * -1 

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = ball_speed_x * -1.01 # Increase speed on paddle hit
        ball_speed_y = ball_speed_y * 1.01


    # Ball reset if out of bounds
    if ball.left <= 0:
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x, ball_speed_y = 3, 3
        right_score = right_score + 1
    if ball.right >= WIDTH: 
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x, ball_speed_y = -3, -3
        left_score = left_score + 1

    # Drawing
    screen.fill(BLACK)
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH//4, 20))
    screen.blit(right_text, (WIDTH*3//4, 20))
    pygame.draw.rect(screen, RED, left_paddle)
    pygame.draw.rect(screen, GREEN, right_paddle)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()