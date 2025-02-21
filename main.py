from settings import *
from player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # RENDER YOUR GAME HERE

    playerX, playerY = 0, 0;
    '''pygame.draw.circle(screen, "red", player_pos, 40)'''
    guy = pygame.image.load("images/guy.png").convert_alpha()
    screen.blit(guy, (player_pos.x, player_pos.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
