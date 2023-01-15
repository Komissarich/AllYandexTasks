#НЕ ПРОВЕРЯЙТЕ
import os
import sys

import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.flip()
screen.fill((0, 0, 0))


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

    def moving(self, direction):
        self.rect.x += direction[0]
        self.rect.y += direction[1]


a = "arrow.png"

car = Car(a)
all_sprites.add(car)

directions = [[10, 0], [-10, 0], [0, 10], [0, -10]]

pygame.display.flip()
fps = 50
v = 60
clock = pygame.time.Clock()
running = True
while running:
    keys = pygame.key.get_pressed()
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        car.rect.x = pygame.mouse.get_pos()[0]
        car.rect.y = pygame.mouse.get_pos()[1]
    else:
        pygame.mouse.set_visible(True)
    pygame.display.update()
    screen.fill((0, 0, 0))

    clock.tick(fps)