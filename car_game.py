import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT  = 500

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame test")

clock = pygame.time.Clock()
player = pygame.image.load("cars\Player.png")
player = pygame.transform.scale(player, (40, 102))
player_Rect = player.get_rect()

player_Rect.centerx = round(SCREEN_WIDTH / 2)
player_Rect.centery = round(SCREEN_HEIGHT / 2)

dx = 0
dy = 0

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            if event.key == pygame.K_RIGHT:
                dx = 5
            if event.key == pygame.K_UP:
                dy = -5
            if event.key == pygame.K_DOWN:
                dy = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0


    SCREEN.fill((255, 255, 255))

    player_Rect.x += dx
    player_Rect.y += dy

    if player_Rect.left < 0:
        player_Rect.left = 0
    if player_Rect.right > SCREEN_WIDTH:
        player_Rect.right = SCREEN_WIDTH
    if player_Rect.top < 0:
        player_Rect.top = 0
    if player_Rect.bottom > SCREEN_HEIGHT:
        player_Rect.bottom = SCREEN_HEIGHT

    """
    if player_Rect.y > SCREEN_HEIGHT:
        player_Rect.y = 0 - player_Rect.height
        # player_Rect.bottom = 0
    """

    SCREEN.blit(player, player_Rect)

    pygame.display.flip()

    clock.tick(60)
 