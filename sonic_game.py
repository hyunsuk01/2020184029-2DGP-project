from os import close

from pico2d import *

Width, Height = 800, 600
open_canvas(Width, Height)

background = load_image('background.png')
map = load_image('map.png')
character = load_image('sonic_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

running = True
frame = 0
char_x = 25
char_y = Height // 2

while running:
    clear_canvas()
    character.clip_draw(frame, 50 * 4, 50, 50, char_x, char_y)
    update_canvas()
    handle_events()

close_canvas()