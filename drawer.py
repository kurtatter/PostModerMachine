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

class Tape(pygame.sprite.Sprite):
    def __init__(self):
        super(Tape, self).__init__()
        PADDING = 4
        self.surf = pygame.Surface((SCREEN_WIDTH*2, 70))
        self.surf.fill((240, 240, 240))
        nums = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
        nums.extend([0, 1, 0, 1, 1, 0, 1, 0, 0, 1])
        start_x = 10
        for n in nums:
            pygame.draw.line(self.surf, (0, 0, 0), [start_x, 10], [start_x, 50])
            start_x += 40
            pygame.draw.line(self.surf, (0, 0, 0), [start_x, 10], [start_x, 50])
            if n:
                pygame.draw.polygon(self.surf, (0, 0, 255),
                                    [[start_x-40+PADDING, 10+PADDING],
                                     [start_x-PADDING, 10+PADDING],
                                     [start_x-PADDING, 50-PADDING],
                                     [start_x-40+PADDING, 50-PADDING]])
        pygame.draw.line(self.surf, (0, 0, 0), [0, 10], [SCREEN_WIDTH*2, 10])
        pygame.draw.line(self.surf, (0, 0, 0), [0, 50], [SCREEN_WIDTH*2, 50])
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tape = Tape()
running = True

nums = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
nums.extend([0, 1, 0, 1, 1, 0, 1, 0, 0, 1])

PADDING = 4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    screen.blit(tape.surf, tape.rect)
    # pygame.draw.line(screen, (255, 255, 0), [0, 50], [800, 50])
    # pygame.draw.line(screen, (255, 255, 0), [0, 100], [800, 100])
    # start_x = 10
    # for n in nums:
    #     pygame.draw.line(screen, (0, 255, 0), [start_x, 50], [start_x, 100])
    #     start_x += 40
    #     pygame.draw.line(screen, (0, 255, 0), [start_x, 50], [start_x, 100])
    #     if n:
    #         pygame.draw.polygon(screen, (255, 255, 255),
    #                             [[start_x-40+PADDING, 50+PADDING],
    #                              [start_x-PADDING, 50+PADDING],
    #                              [start_x-PADDING, 100-PADDING],
    #                              [start_x-40+PADDING, 100-PADDING]])
    pressed_keys = pygame.key.get_pressed()
    tape.update(pressed_keys)

    pygame.display.flip()