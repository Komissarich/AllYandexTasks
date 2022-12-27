import os
import sys

import pygame


pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):

        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

all_sprites = pygame.sprite.Group()


class End_Screen(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()

        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = -400




screen1 = End_Screen("gameover.png")
all_sprites.add(screen1)

direction = True

pygame.display.flip()

v = 200
clock = pygame.time.Clock()
running = True
while running:
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if screen1.rect.x < 0:
        screen1.rect.x += v * clock.tick() / 1000

    pygame.display.update()

    screen.fill((255, 255, 255))

