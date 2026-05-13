import pygame 
pygame.init()

window = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Study café")

run = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()