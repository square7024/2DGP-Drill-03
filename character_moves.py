from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_rectengle():
    print("Moving rectengle")
    pass


def move_circle():
    print("Moving circle")
    clear_canvas_now()
    boy.draw_now(400, 300)
    delay(0.1)
    pass


while True:
    move_circle()
    move_rectengle()
    # break
    pass

close_canvas()
