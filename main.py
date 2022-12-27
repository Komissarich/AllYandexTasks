import os
import sys

import pygame

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
pygame.display.flip()
screen.fill((255, 255, 255))


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


all_sprites = pygame.sprite.Group()


class Car(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()

        self.image = load_image(name)

        self.rect = self.image.get_rect()
        self.car_right = self.image
        self.car_left = pygame.transform.flip(self.car_right, True, False)

    def moving(self, direction1):

        if direction1:
            self.image = self.car_right
            self.rect.x += 1
        else:
            self.image = self.car_left
            self.rect.x -= 1


a = "car2.png"

car = Car(a)
all_sprites.add(car)

direction = True

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
    if car.rect.x > 455:
        direction = False
    if car.rect.x < 10:
        direction = True

    car.moving(direction)

    pygame.display.update()
    screen.fill((255, 255, 255))

    clock.tick(fps)
