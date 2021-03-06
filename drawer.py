import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class ConsoleTerminal(pygame.sprite.Sprite):
    def __init__(self):
        super(ConsoleTerminal).__init__()
        self.surf = pygame.Surface((400, 120))
        self.rect = self.surf.get_rect()
        self.surf.fill((77, 77, 77))


class Carret(pygame.sprite.Sprite):
    def __init__(self):
        super(Carret, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        pygame.draw.polygon(self.surf, (255, 255, 255),
                            [[0, 0], [50, 0],
                             [25, 50], [25, 50]])

    # def update(self, pressed_keys):
    #     # if pressed_keys[K_UP]:
    #     #     self.rect.move_ip(0, -1)
    #     if pressed_keys[K_DOWN]:
    #         print("self.start_x", self.rect.x)
    #         pygame.display.flip()


class Tape(pygame.sprite.Sprite):
    CARRET_X = 0

    def __init__(self, nums):
        super(Tape, self).__init__()
        self.PADDING = 4
        self.COLOR_BLUE = (0, 0, 255)
        self.COLOR_WHITE = (255, 255, 255)
        self.surf = pygame.Surface((SCREEN_WIDTH * 11, 70))
        self.surf.fill((240, 240, 240))
        self.font = pygame.font.SysFont("Arial", 12)
        # self.textSurf = self.font.render('Aloha', 1, (0,0,0))
        # self.surf.blit(self.textSurf, [20, 55])
        self.start_x = 10
        self.coords = []
        for i, n in enumerate(nums):
            pygame.draw.line(self.surf, (0, 0, 0), [self.start_x, 10], [self.start_x, 50])
            self.textSurf = self.font.render(str(i), 1, (0, 0, 0))
            self.surf.blit(self.textSurf, [(self.start_x - self.textSurf.get_width() / 2 + 20), 55])
            if i == 0:
                self.CARRET_X = (self.start_x - self.textSurf.get_width() / 2 + 20)
            self.start_x += 40
            pygame.draw.line(self.surf, (0, 0, 0), [self.start_x, 10], [self.start_x, 50])
            if n:
                self.coords.append([[self.start_x - 40 + self.PADDING, 10 + self.PADDING],
                                     [self.start_x - self.PADDING, 10 + self.PADDING],
                                     [self.start_x - self.PADDING, 50 - self.PADDING],
                                     [self.start_x - 40 + self.PADDING, 50 - self.PADDING]])
                pygame.draw.polygon(self.surf, self.COLOR_BLUE,
                                    [[self.start_x - 40 + self.PADDING, 10 + self.PADDING],
                                     [self.start_x - self.PADDING, 10 + self.PADDING],
                                     [self.start_x - self.PADDING, 50 - self.PADDING],
                                     [self.start_x - 40 + self.PADDING, 50 - self.PADDING]])
            else:
                self.coords.append([[self.start_x - 40 + self.PADDING, 10 + self.PADDING],
                                    [self.start_x - self.PADDING, 10 + self.PADDING],
                                    [self.start_x - self.PADDING, 50 - self.PADDING],
                                    [self.start_x - 40 + self.PADDING, 50 - self.PADDING]])
        pygame.draw.line(self.surf, (0, 0, 0), [0, 10], [SCREEN_WIDTH * 11, 10])
        pygame.draw.line(self.surf, (0, 0, 0), [0, 50], [SCREEN_WIDTH * 11, 50])
        self.rect = self.surf.get_rect()
        self.rect.y = 100

    def update(self, pressed_keys):
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            # nums[cell_number] = 1 if nums[cell_number] == 0 else 0
            # print("self.start_x", self.rect.x)
            # pygame.draw.polygon(self.surf, (0, 255, 255),
            #                     [[80 - 40 + self.PADDING, 10 + self.PADDING],
            #                      [80 - self.PADDING, 10 + self.PADDING],
            #                      [80 - self.PADDING, 50 - self.PADDING],
            #                      [80 - 40 + self.PADDING, 50 - self.PADDING]])
            if nums[cell_number]:
                nums[cell_number] = 0
                pygame.draw.polygon(self.surf, self.COLOR_WHITE,self.coords[cell_number])
                pygame.time.wait(200)
            else:
                nums[cell_number] = 1
                pygame.draw.polygon(self.surf, self.COLOR_BLUE, self.coords[cell_number])
                pygame.time.wait(200)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(40, 0)
            pygame.time.wait(200)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(-40, 0)
            pygame.time.wait(200)

        if self.rect.right < SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left > 0:
            self.rect.left = 0


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
nums = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1] * 20
nums.append(0)
tape = Tape(nums=nums)
carret = Carret()
terminal = ConsoleTerminal()
running = True

PADDING = 4

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key == K_DOWN:
            #     screen.up

    screen.fill((0, 0, 0))
    screen.blit(tape.surf, tape.rect)
    surf_carret_center = (
        # (SCREEN_WIDTH - carret.surf.get_width()) / 2,
        tape.CARRET_X - 20,
        40
    )
    screen.blit(carret.surf, surf_carret_center)
    screen.blit(terminal.surf, terminal.rect)
    cell_number = abs(tape.rect.x // 40)
    # print(abs(tape.rect.x // 40), bool(nums[cell_number]))
    # pygame.draw.line(screen, (255, 255, 0), [0, 50], [800, 50])
    # pygame.draw.line(screen, (255, 255, 0), [0, 100], [800, 100])
    # self.start_x = 10
    # for n in nums:
    #     pygame.draw.line(screen, (0, 255, 0), [self.start_x, 50], [self.start_x, 100])
    #     self.start_x += 40
    #     pygame.draw.line(screen, (0, 255, 0), [self.start_x, 50], [self.start_x, 100])
    #     if n:
    #         pygame.draw.polygon(screen, (255, 255, 255),
    #                             [[self.start_x-40+self.PADDING, 50+self.PADDING],
    #                              [self.start_x-self.PADDING, 50+self.PADDING],
    #                              [self.start_x-self.PADDING, 100-self.PADDING],
    #                              [self.start_x-40+self.PADDING, 100-self.PADDING]])
    pressed_keys = pygame.key.get_pressed()
    tape.update(pressed_keys)
    carret.update(pressed_keys)

    pygame.display.flip()
    clock.tick(60)
