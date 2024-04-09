import pygame 
from pygame.locals import *
import sys

# initialising the game 
pygame.init()

# define the window dimensions
window_width = 800
window_height = 400

# create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# creating the game objects
# define the colours
black = (0, 0, 0)
white = (255, 255, 255)

# paddle dimensions
paddle_width = 10
paddle_height = 60

#create the paddles
paddle1 = pygame.Rect(50, 150, paddle_width, paddle_height)
paddle2 = pygame.Rect(window_width - 50 - paddle_width, 150, paddle_width, paddle_height)

# create the ball
ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)

# initial ball speed
ball_speed_x = 3
ball_speed_y = 3

# initial paddle speed
paddle_speed = 5

# initial score
score1 = 0
score2 = 0

# create a font for displaying the scores
font = pygame.font.Font(None, 36)

# creat clock object to control the framerate
clock = pygame.time.Clock()

# implementing game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # moving the paddels
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1.y > 0:
        paddle1.y -= paddle_speed
    if keys[K_s] and paddle1.y < window_height - paddle_height:
        paddle1.y += paddle_speed
    if keys[K_UP] and paddle2.y > 0:
        paddle2.y -= paddle_speed
    if keys[K_DOWN] and paddle2.y < window_height - paddle_height:
        paddle2.y += paddle_speed
    
    # moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # ball collision with top and bottom of the screen
    if ball.bottom <= 0 or ball.top >= window_height:
        ball_speed_y *= -1

    # ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # check if ball goes out of bounds
    if ball.left <= 0:
        score2 += 1 #add one to player 2 score
        ball.center = (window_width // 2, window_height // 2) # reset to middle
        ball_speed_x *= -1
    elif ball.right >= window_width:
        score1 += 1 #add one to player 1 score
        ball.center = (window_width // 2, window_height // 2) # reset to middle
        ball_speed_x *= -1
        

    # clear the screen
    window.fill(black)

    # draw the paddles
    pygame.draw.rect(window, white, paddle1)
    pygame.draw.rect(window, white, paddle2)

    # draw the ball
    pygame.draw.rect(window, white, ball)

    # draw the score
    score_text = font.render(f"{score1} - {score2}", True, white)
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 10))

    # update the screen
    pygame.display.flip()

    # contol the framerate 
    clock.tick(60) # set framerate to 60 fps