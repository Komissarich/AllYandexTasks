import os
import sys
import random
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.flip()


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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        a = load_image(name)
        a1 = pygame.transform.scale(a, (100, 100))
        self.image = a1
        self.rect = self.image.get_rect()

        self.boomed = False

    def change_img(self):
        if self.boomed is not True:
            self.boomed = True
            x = self.rect.x
            y = self.rect.y
            all_sprites.remove(self)

            b = load_image("boom.png")
            self.image = b
            bombs_sprites.add(self)
            all_sprites.update()
            bombs_sprites.update()
            all_sprites.draw(screen)
            bombs_sprites.draw(screen)




bombs_sprites = pygame.sprite.Group()
bombs = []
for i in range(20):
    x = random.randrange(10, 400)
    y = random.randrange(10, 400)
    boom = Bomb("bomb.png")
    boom.rect.x = x
    boom.rect.y = y
    bombs.append(boom)
    all_sprites.add(boom)

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in bombs if s.rect.collidepoint(pos)]
            for i in clicked_sprites:
                i.change_img()

    all_sprites.update()
    all_sprites.draw(screen)
    bombs_sprites.update()
    bombs_sprites.draw(screen)


    pygame.display.flip()

