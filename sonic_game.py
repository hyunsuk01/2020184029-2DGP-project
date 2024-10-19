from os import close

from pico2d import *

Width, Height = 800, 600
open_canvas(Width, Height)

background = load_image('background.png')
map = load_image('map.png')
character = load_image('sonic_sheet.png')

def handle_events():
    global running, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir = 1
            elif event.key == SDLK_LEFT:
                dir = -1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = 0
            elif event.key == SDLK_LEFT:
                dir = 0

running = True
dir = 0

frame = 0
char_x = 25
char_y = Height // 2
char_speed = 5

bg_x = 0
bg_speed = 3840 / 5120 #background 이미지 가로 / map 이미지 가로

map_x = 0
map_y = 100
map_speed = 5

while running:
    clear_canvas()
    background.clip_draw(int(bg_x), 0, Width, Height, Width // 2, Height // 2)
    map.clip_draw(map_x, map_y, Width, Height, Width // 2, Height // 2)
    character.clip_draw(frame, 50 * 4, 50, 50, char_x, char_y)
    update_canvas()
    handle_events()

close_canvas()