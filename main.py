import pygame

pygame.init()
size = weight, height = (800, 450)
screen = pygame.display.set_mode(size)

fps = 330
clock = pygame.time.Clock()
running = True

while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
