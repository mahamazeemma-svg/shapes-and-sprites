import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hollow and Solid Ball")
screen.fill((255, 255, 255))
GREEN = (0, 255, 0)
pygame.draw.circle(screen, GREEN, (300, 300), 50)
pygame.draw.circle(screen, GREEN, (100, 100), 50, 3)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()