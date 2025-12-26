import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пустая кнопка без эффекта клика")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

button_rect = pygame.Rect(150, 120, 100, 50)  # x, y, width, height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Кнопка нажата!")
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, button_rect)
    pygame.display.update()

pygame.quit()
sys.exit()
