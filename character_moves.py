from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_rectengle():
    print("Moving rectengle")
    pass


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)
    pass


while True:
    move_circle()
    move_rectengle()
    break
    # pass

close_canvas()
