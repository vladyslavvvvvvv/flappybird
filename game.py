import pygame 


WIDTH = 1300
HEIGHT = 600

SIZE = (WIDTH,HEIGHT)

window = pygame.display.set_mode(SIZE)
background_color = (60, 160, 65)
window.fill(background_color)
clock = pygame.time.Clock()





game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)



