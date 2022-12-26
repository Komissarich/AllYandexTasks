import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.a = 0
        self.colors = [[255, 255, 255], [255, 0, 0], [0, 0, 255]]
        self.board = [[self.colors[0]] * width for _ in range(height)]
        print(self.board)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def changecolor(self, x, y):
        self.a += 1
        for y1 in range(self.height):
            for x1 in range(self.width):
                if x1 == x and y1 == y:
                    self.board[y1][x1] = self.colors[self.a % 3]


    def render(self, screen):

        for y1 in range(self.height):
            for x1 in range(self.width):
                if self.board[y1][x1] == [255, 255, 255]:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x1 * self.cell_size + self.left, y1 * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, tuple(self.board[y1][x1]), (
                        x1 * self.cell_size + self.left, y1 * self.cell_size + self.top, self.cell_size,
                        self.cell_size))




pygame.init()
screen = pygame.display.set_mode((300, 300))
board = Board(5, 7)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x = round((x - 10) // 30)
            y = round((y - 10) // 30)
            screen.fill((0, 0, 0))
            board.changecolor(x, y)


    board.render(screen)
    pygame.display.flip()
