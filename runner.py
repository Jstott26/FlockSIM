import pygame
import numpy
import boid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# variables
half_width = screen.get_width() / 2
half_height = screen.get_height() / 2

# objects
boid = boid.boid(half_width, half_height, 0, 0)

player_pos = pygame.Vector2(half_width, half_height)
# Main loop
while running:
# -------------------------------------------------------------------
# Events tab
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        boid.changepos(boid.posx, boid.posy - 300 * dt)
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    if player_pos.y - boid.height <= 0:
        player_pos.y = 0 + boid.height
    if player_pos.y + boid.height >= screen.get_height():
        player_pos.y = screen.get_height() - boid.height
    if player_pos.x <= 0:
        player_pos.x = 0
    if player_pos.x + boid.length >= screen.get_width():
        player_pos.x = screen.get_width() - boid.length

# -------------------------------------------------------------------
# Draw tab
    screen.fill("white")

# -------------------------------------------------------------------
# Update
    pygame.display.flip()
# Frame tick
    dt = clock.tick(60) / 1000

pygame.quit()

def createboid(screen):
    boid_pos = pygame.Vector2(boid.posx, boid.posy)
    pygame.draw.polygon(screen,(0, 0, 255), [boid_pos,
            (boid_pos.x + boid.length, boid_pos.y + boid.height),
            (boid_pos.x + boid.length, boid_pos.y - boid.height)]
    )
