import pygame

pygame.init()

# Create the screen

screen = pygame.display.set_mode((600,800))

# Set title and icon

pygame.display.set_caption("Quang Huy")
icon = pygame.image.load('mars.png')
pygame.display.set_icon(icon)
playerx = 270
playery = 600
speed = 0
# Player
playerImg = pygame.image.load('Su 47.png')

def Player(x,y):
    screen.blit(playerImg,(x,y))

def change_direction(new_di):
    pass

# Loop
running = True
while running:
    # Set background screen
    screen.fill('#03fce3')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed = -0.3
            if event.key == pygame.K_d:
                speed = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                speed = 0

    playerx += speed
    Player(playerx ,playery)
    pygame.display.update()
