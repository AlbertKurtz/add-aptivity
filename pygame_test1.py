import pygame

background_color = (255, 255, 255)
(width,  height) = (300, 200)


screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Test 1")

screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False