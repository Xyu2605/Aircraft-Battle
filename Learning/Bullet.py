import pygame

class Bullet:

    def __init__(self, pos_x, pos_y, speed):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.rotate(self.image,90)

    def update(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
        self.pos_y -= self.speed

