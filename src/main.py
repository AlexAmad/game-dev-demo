import sys

import pygame

pygame.init()


# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Project")

BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Initial position of the rectangle
rect_x, rect_y = 100, 100
rect_speed = 5  # Speed of movement

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Move the rectangle based on key presses
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw the red rectangle at the updated position
    pygame.draw.rect(screen, RED, pygame.Rect(rect_x, rect_y, 200, 200))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()