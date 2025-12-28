import pygame as pg

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:  # RRGGBB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
    elif len(hex_color) == 8:  # RRGGBBAA
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        a = int(hex_color[6:8], 16)
        return (r, g, b, a)
    else:
        raise ValueError("Неверный формат HEX")

pg.init()
screen = pg.display.set_mode((800, 600))
WIDTH, HEIGHT = screen.get_size()
print(f"WIDTH: {WIDTH}, HEIGHT: {HEIGHT}")

LayotScreens = []
def LayotScreenAdd(screen):
    LayotScreens.append(screen)
def LayotScreenSet(screen):
    LayotScreens.clear()
    LayotScreenAdd(screen)

running = True
while running:
    screen.fill(hex_to_rgb("#252525FF"))
    WIDTH, HEIGHT = screen.get_size()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(f"x: {x}, y: {y}")

    pg.display.flip()

pg.quit()
