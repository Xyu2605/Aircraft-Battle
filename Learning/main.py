import pygame
import random
from Bullet import *
pygame.init()

# Create the screen

screen = pygame.display.set_mode((800,600))
back_ground = pygame.image.load('map.png')
# Set title and icon

pygame.display.set_caption("Quang Huy")
icon = pygame.image.load('mars.png')
pygame.display.set_icon(icon)

# Player
playerx = 270
playery = 500
speed = 0


playerImg = pygame.image.load('F 22.png')
playerImg = pygame.transform.rotate(playerImg, 45)

def Player(x,y):
    damage = 50
    # playerImg = pygame.transform.smoothscale(playerImg, (60, playerImg.get_height()))  
    screen.blit(playerImg,(x,y))

def Player_moves(event, speed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            speed = -2
        if event.key == pygame.K_d:
            speed = 2
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
            speed = 0

    return speed
# Enemy
enemyx = random.randint(0,536)
enemyy = -64
e_speed = 1
enemyImg = pygame.image.load('enemy.png')


def Enemy(x,y):
    screen.blit(enemyImg, (x, y))

def Enemy_moves(y,e_speed):
    pass

bullets = []
bullet_state = "none"

def shooting(event, x, y):
    global bullet_state
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            bullet_state = "fire"
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            bullet_state = "none"

            
            
# Loop
running = True
fire_cool_down = 0.2
FPS = 120

while running:
    # Set background screen
    pygame.time.Clock().tick(FPS)
    screen.blit(back_ground,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        speed = Player_moves(event, speed)
        shooting(event, playerx, playery)

    if bullet_state == "fire" and fire_cool_down <= 0:
        fire_cool_down = 0.1
        bullets.append(Bullet(playerx + 14, playery + 10, 5))
        bullets.append(Bullet(playerx + 53, playery + 10, 5))


    enemyy += e_speed
    # if enemyx <= 0:
    #     e_speed += 0.5
    # if enemyx >= 736:
    #     e_speed -= 0.5
    playerx += speed
    if playerx <= -20:
        playerx = -20
    elif playerx >= 730:
        playerx = 730
    Player(playerx ,playery)
    Enemy(enemyx,enemyy)
    for bullet in bullets:
        bullet.update(screen)
        if bullet.pos_y < 0:
            bullets.remove(bullet)
    if fire_cool_down > 0:
        fire_cool_down -= (1/FPS)
    pygame.display.update()
