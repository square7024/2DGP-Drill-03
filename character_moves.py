from pico2d import *

open_canvas()

boy = load_image('character.png')

top = 560
right = 780

def move_top():
    print('Moving top')
    for x in range(right, 0, -5):
        draw_boy(x, top)
    pass


def move_right():
    print('Moving right')
    for y in range(0, top, 5):
        draw_boy(right, y)
    pass


def move_bottom():
    print('Moving bottom')
    pass


def move_left():
    print('Moving left')
    pass


def move_rectengle():
    print("Moving rectengle")
    move_right()
    move_top()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # move_circle()
    move_rectengle()
    break
    pass

close_canvas()
