from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

top = 560
right = 780
bottom = 80
left = 20
center_x = (right + left) // 2
center_y = (top + bottom) // 2

# 캐릭터를 그리는 함수
def draw_boy(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(int(x), int(y))
    delay(0.01)

# 사각형 운동

def move_rectangle():
    # 1. 아래쪽(가운데->오른쪽)
    for x in range(center_x, right + 1, 5):
        draw_boy(x, bottom)
    # 2. 오른쪽(아래->위)
    for y in range(bottom, top + 1, 5):
        draw_boy(right, y)
    # 3. 위쪽(오른쪽->왼쪽)
    for x in range(right, left - 1, -5):
        draw_boy(x, top)
    # 4. 왼쪽(위->아래)
    for y in range(top, bottom + 1, -5):
        draw_boy(left, y)
    # 5. 아래쪽(왼쪽->가운데)
    for x in range(left, center_x + 1, 5):
        draw_boy(x, bottom)

# 원 운동

def move_circle():
    r = (top - bottom) // 2
    # 270도(아래)에서 시작해서 360도 회전
    for deg in range(270, 630, 3):
        x = center_x + r * math.cos(math.radians(deg))
        y = center_y + r * math.sin(math.radians(deg))
        draw_boy(x, y)
    # 마지막에 정확히 (center_x, bottom) 위치로 복귀
    draw_boy(center_x, bottom)

# 삼각형 운동

def move_triangle():
    # 1. (가운데, bottom) -> (오른쪽, bottom)
    for x in range(center_x, right + 1, 5):
        draw_boy(x, bottom)
    # 2. (오른쪽, bottom) -> (center_x, top)
    for i in range(0, 101, 2):
        x = right - (right - center_x) * i / 100
        y = bottom + (top - bottom) * i / 100
        draw_boy(x, y)
    # 3. (center_x, top) -> (center_x, bottom)
    for y in range(top, bottom - 1, -5):
        draw_boy(center_x, y)

while True:
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()
