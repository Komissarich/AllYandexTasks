import os
import sys

import pygame
import random
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.flip()
screen.fill((255, 255, 255))

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
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

class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height

class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


mountain = Mountain()


a = []
pygame.display.flip()
fps = 50
v = 60
clock = pygame.time.Clock()
running = True
while running:
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a.append(Landing(event.pos))
    for i in a:
        i.update()

    pygame.display.update()
    screen.fill((255, 255, 255))

    clock.tick(fps)
