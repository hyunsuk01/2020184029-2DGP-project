from os import close

from pico2d import *

Width, Height = 1280, 1024
open_canvas(Width, Height)

background = load_image('background.png')
map = load_image('map.png')
character = load_image('sonic_sheet.png')

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir_x = 1
            elif event.key == SDLK_LEFT:
                dir_x = -1
            elif event.key == SDLK_UP:
                dir_y = 1
            elif event.key == SDLK_DOWN:
                dir_y = -1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x = 0
            elif event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_UP:
                dir_y = 0
            elif event.key == SDLK_DOWN:
                dir_y = 0

running = True
dir_x = 0
dir_y = 0

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

    clip_w = int(Width / 3)
    clip_h = int(Height / 3)
    if map_y < 0:
        map_y = 0
    elif map_y + clip_h > map.h:
        map_y = map.h - clip_h

    map.clip_draw(map_x, map_y, clip_w, clip_h, Width // 2, Height // 2, Width, Height)
    character.clip_draw(frame, 50 * 4, 50, 50, char_x, char_y, 100, 100)
    update_canvas()
    handle_events()

    if dir_x == 1:
        if char_x >= Width // 2 and bg_x < 3840 - Width:
            bg_x += char_speed * bg_speed
            map_x += char_speed
        elif char_x < Width - 25:
            char_x += char_speed
    elif dir_x == -1:
        if char_x <= Width // 2 and bg_x > 0:
            bg_x -= char_speed * bg_speed
            map_x -= char_speed
        elif char_x > 25:
            char_x -= char_speed
    elif dir_y == 1:
        map_y += map_speed
    elif dir_y == -1:
        map_y -= map_speed

    delay(0.01)

close_canvas()