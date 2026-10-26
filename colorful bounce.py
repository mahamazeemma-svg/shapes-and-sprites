import pygame
import random

pygame.init()

SPRITE_EVENT_CHANGE = pygame.USEREVENT + 1
BACKGROUND_EVENT_CHANGE = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
DARK_BLUE = pygame.Color('darkblue')
LIGHT_BLUE = pygame.Color('lightblue')

MAGENTA = pygame.Color('magenta')
YELLOW = pygame.Color('yellow')
WHITE = pygame.Color('white')
ORANGE = pygame.Color('orange')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1), random.randint(-1, 1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True

        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_EVENT_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_EVENT_CHANGE))
    def color_change(self, color):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def background_color_change():
    global bgcolor 
    bgcolor = random.choice([BLUE, DARK_BLUE, LIGHT_BLUE])

all_sprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")
bgcolor = BLUE
screen.fill(bgcolor)

exit = False

clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_EVENT_CHANGE:
            sp1.color_change(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
        elif event.type == BACKGROUND_EVENT_CHANGE:
            background_color_change()

    all_sprites.update()

    screen.fill(bgcolor)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()