import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
widowicon = pygame.image.load("refresh_icon_188574.png")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
pygame.display.set_caption("Hello World") # 윈도 타이틀 설정
pygame.display.set_icon(widowicon) # 윈도 아이콘 설정
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 윈도 스크린 크기 설정

key_left_color = red
key_right_color = red
key_up_color = red
key_down_color = red

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:key_left_color = green
            if event.key == pygame.K_RIGHT:key_right_color = green
            if event.key == pygame.K_UP:key_up_color = green
            if event.key == pygame.K_DOWN:key_down_color = green

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:key_left_color = red
            if event.key == pygame.K_RIGHT:key_right_color = red
            if event.key == pygame.K_UP:key_up_color = red
            if event.key == pygame.K_DOWN:key_down_color = red

        pygame.draw.circle(SCREEN, key_left_color, (150,250), 20)
        pygame.draw.circle(SCREEN, key_right_color, (250,250), 20)
        pygame.draw.circle(SCREEN, key_up_color, (200,200), 20)
        pygame.draw.circle(SCREEN, key_down_color, (200,250), 20)
        pygame.display.update()