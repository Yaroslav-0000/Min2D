import pygame as pg

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    elif len(hex_color) == 8:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
    else:
        raise ValueError("Неверный формат HEX")

pg.init()

screen = pg.display.set_mode((800, 600))
WIDTH, HEIGHT = screen.get_size()
print(f"WIDTH: {WIDTH}, HEIGHT: {HEIGHT}")

font = pg.font.SysFont(None, int(HEIGHT * 0.06))

# ─── СИСТЕМА ЭКРАНОВ ────────────────────────
current_screen = None

def set_screen(name):
    global current_screen
    current_screen = name

# ─── ЭКРАНЫ (RENDER-ФУНКЦИИ) ─────────────────
def render_game(screen, events):
    screen.fill(hex_to_rgb("#252525FF"))
    pg.draw.rect(screen, hex_to_rgb("#3A6EFF"), pg.Rect(
        int(WIDTH * 0.8),
        int(HEIGHT * 0.05),
        int(WIDTH * 0.15),
        int(HEIGHT * 0.08)
    ), border_radius=0)

    txt = font.render("MENU", True, hex_to_rgb("#752222"))
    screen.blit(txt, txt.get_rect(center=pg.Rect(
        int(WIDTH * 0.8),
        int(HEIGHT * 0.05),
        int(WIDTH * 0.15),
        int(HEIGHT * 0.08)
    ).center))

    for e in events:
        if e.type == pg.MOUSEBUTTONDOWN:
            if pg.Rect(
                int(WIDTH * 0.8),
                int(HEIGHT * 0.05),
                int(WIDTH * 0.15),
                int(HEIGHT * 0.08)
            ).collidepoint(e.pos):
                set_screen("game_menu")

def render_game_menu(screen, events):
    # затемнение поверх игры
    overlay = pg.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(160)
    overlay.fill((0,0,0))
    screen.blit(overlay, (0, 0))
    pg.draw.rect(screen, hex_to_rgb("#FF0000"), pg.Rect(
        int(WIDTH * 0.1),
        int(HEIGHT * 0.25),
        int(WIDTH * 0.8),
        int(HEIGHT * 0.5)
    ), border_radius=0)

    txt = font.render("CLOSE", True, hex_to_rgb("#0E9395"))
    txt_rect = txt.get_rect(center=pg.Rect(
        int(WIDTH * 0.1),
        int(HEIGHT * 0.25),
        int(WIDTH * 0.8),
        int(HEIGHT * 0.5)
    ).center)
    screen.blit(txt, txt_rect)

    for e in events:
        if e.type == pg.MOUSEBUTTONDOWN:
            if pg.Rect(
                int(WIDTH * 0.1),
                int(HEIGHT * 0.25),
                int(WIDTH * 0.8),
                int(HEIGHT * 0.5)
            ).collidepoint(e.pos):
                set_screen("game")

# ─── РЕГИСТР ЭКРАНОВ ─────────────────────────
screens = {
    "game": render_game,
    "game_menu": render_game_menu
}

set_screen("game")

# ─── ГЛАВНЫЙ ЦИКЛ ────────────────────────────
running = True
while running:
    WIDTH, HEIGHT = screen.get_size()
    events = pg.event.get()

    for e in events:
        if e.type == pg.QUIT:
            running = False

    screens[current_screen](screen, events)

    pg.display.flip()

pg.quit()
