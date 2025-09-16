from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

top = 560
right = 780
bottom = 80
left = 20
center_x = (right + bottom) // 2
center_y = (top + bottom) // 2

def move_top():
    print('Moving top')
    for x in range(right, left, -5):
        draw_boy(x, top)
    pass


def move_right():
    print('Moving right')
    for y in range(bottom, top, 5):
        draw_boy(right, y)
    pass


def move_bottom1():
    print('Moving bottom')
    for x in range(center_x, right, 5):
        draw_boy(x, bottom)
    pass


def move_left():
    print('Moving left')
    for y in range(top, bottom, -5):
        draw_boy(left, y)
    pass


def move_bottom2():
    print('Moving bottom')
    for x in range(left, center_x, 5):
        draw_boy(x, bottom)
    pass


def move_rectengle():
    print("Moving rectengle")
    move_bottom1()
    move_right()
    move_top()
    move_left()
    move_bottom2()
    pass


def move_circle():
    print("Moving circle")
    r = (top - bottom) / 2
    for deg in range(90, 360 + 90):
        x = r * math.cos(math.radians(deg)) + center_x
        y = r * math.sin(math.radians(deg - 180)) + center_y
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)


def move_tri_left_base():
    for x in range(center_x, left, -5):
        draw_boy(x, bottom)
    pass


def move_tri_left_side():
    for x in range(left, center_x, 3):
        y = ((top - bottom) / (center_x - left)) * (x - left) + bottom
        draw_boy(x, y)
    pass


def move_tri_right_side():
    for x in range(center_x, right, 3):
        y = ((top - bottom) / (center_x - right)) * (x - right) + bottom
        draw_boy(x, y)
    pass


def move_tri_right_base():
    for x in range(right, center_x, -5):
        draw_boy(x, bottom)
    pass


def move_triangle():
    print("Moving triangle")
    move_tri_left_base()
    move_tri_left_side()
    move_tri_right_side()
    move_tri_right_base()
    pass


while True:
    move_rectengle()
    move_triangle()
    move_circle()
    pass

close_canvas()
