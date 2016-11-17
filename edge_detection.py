# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Edge Detection"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

    
# Make a block
block_x = 375
block_y = 275
block_size = 50

block_vx = 0
block_vy = 0

block_speed = 5

# Select test case
'''
1 = stop on edge
2 = wrap around
'''
case = 1


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]

    if up:
        block_v_y = -block_speed
    elif down:
        block_v_y = block_speed
    else:
        block_v_y = 0
        
    if left:
        block_v_x = -block_speed
    elif right:
        block_v_x = block_speed
    else:
        block_v_x = 0

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the block '''
    block_x += block_v_x
    block_y += block_v_y

    ''' get block edges (makes collision resolution easier to read) '''

    
    if case == 1:
        ''' if the block is moved out of the window, nudge it back on. '''
        pass

    
    elif case == 2:
        ''' if the block is moved completely off of the window, reposition it on the other side '''
        pass


    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [block_x, block_y, block_size, block_size])


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
