import sys

import pygame

pygame.init()


# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Project")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill screen with white
    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()