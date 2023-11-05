import pygame 
from random import randint


WIDTH = 1300
HEIGHT = 600

SIZE = (WIDTH,HEIGHT)

window = pygame.display.set_mode(SIZE)
background_color = (60, 160, 65)
background_image = pygame.transform.scale(pygame.image.load("background.png"), SIZE)

score = 0

pygame.font.init()
font2 = pygame.font.Font(None, 40)



window.fill(background_color)
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size, speed):
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.original = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bird(GameSprite):
    def update(self):
        self.rect.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.y -= self.speed*2

class Tube(GameSprite):
    def update_up(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = WIDTH + randint(0,100)
            self.rect = pygame.Rect(self.rect.x,self.rect.y, self.rect.width, randint(50,HEIGHT/2-50))
            self.image = pygame.Surface(size=(self.rect.width, self.rect.height))
            self.image = pygame.transform.scale(self.original, (self.rect.width,self.rect.height))
            global score
            score += 1
            self.speed = randint(3,10)

    def update_down(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = WIDTH + randint(0,100)
            self.rect = pygame.Rect(self.rect.x, randint(HEIGHT/2, HEIGHT-100), self.rect.width, self.rect.height)
            self.image = pygame.Surface(size=(self.rect.width, self.rect.height))
            self.image = pygame.transform.scale(self.original, (self.rect.width,self.rect.height))
            global score
            score += 1
            self.speed = randint(3,10)

bird = Bird("bird.png", (50, HEIGHT/2), (50,50), 4)
up_tube = Tube("tube_up.png", (WIDTH, 100), (75, 200), 4)
down_tube = Tube("tube_down.png", (WIDTH, HEIGHT+100), (75, 600), 4)

game = True
finish = False
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not finish:
        window.blit(background_image, (0,0))
        bird.update()
        bird.reset()
        up_tube.update_up()
        up_tube.reset()
        down_tube.update_down()
        down_tube.reset()

        if pygame.sprite.collide_rect(bird,up_tube) or pygame.sprite.collide_rect(bird,down_tube):
            finish = True
            pygame.font.init()
            font1 = pygame.font.Font(None,60)
            text = font1.render("Ти програв", True, (255,0,0))
            window.blit(text, (WIDTH/2-100, HEIGHT/2))

        score_text = font2.render(str(score), True, (255,255,255))
        window.blit(score_text, (0,0))

    pygame.display.update()
    clock.tick(60)