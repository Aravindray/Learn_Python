import pygame
import sys
import random

BLACK = (0, 0, 0)
WINDOWS_WIDTH =640
WINDOWS_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_MOVE = 5

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
clock = pygame.time.Clock()

ball_image = pygame.image.load('images/ball.png')
bounce_sound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

ball_rect = ball_image.get_rect()
MAX_WIDTH = WINDOWS_WIDTH - ball_rect.width
MAX_HEIGHT = WINDOWS_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_MOVE
y_speed = N_PIXELS_MOVE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if (ball_rect.left < 0) or (ball_rect.right >= WINDOWS_WIDTH):
        x_speed = -x_speed
        bounce_sound.play()

    if (ball_rect.top < 0) or (ball_rect.bottom >= WINDOWS_HEIGHT):
        y_speed = -y_speed
        bounce_sound.play()

    ball_rect.left = ball_rect.left + x_speed
    ball_rect.top = ball_rect.top + y_speed

    window.fill(BLACK)

    window.blit(ball_image, ball_rect)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
