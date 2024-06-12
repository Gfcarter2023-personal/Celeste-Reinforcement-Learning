import pydirectinput
import pyautogui
import time


def initialize():
    windows = pyautogui.getWindowsWithTitle('Celeste')
    for window in windows:
        if window.title == 'Celeste':
            window.maximize()



def right(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("right")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("right")


def left(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("left")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("left")


def up(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("up")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("up")


def down(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("down")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("down")

def upRight(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("right")
    pydirectinput.keyDown("up")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("right")
    pydirectinput.keyUp("up")


def upLeft(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("left")
    pydirectinput.keyDown("up")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("left")
    pydirectinput.keyUp("up")


def downRight(sleep_time, doDash=False, doJump =False):
    pydirectinput.keyDown("right")
    pydirectinput.keyDown("down")
    if doDash:
        dash()
    if doJump:
        jump()
    time.sleep(sleep_time)
    pydirectinput.keyUp("right")
    pydirectinput.keyUp("down")


def downLeft(sleep_time, doDash=False, doJump =0):
    pydirectinput.keyDown("left")
    pydirectinput.keyDown("down")
    if doDash:
        dash()
    if doJump > 0:
        jump(doJump)
    time.sleep(sleep_time)
    pydirectinput.keyUp("left")
    pydirectinput.keyUp("down")


def jump(jumpStr):
    pydirectinput.keyDown("c")
    time.sleep(jumpStr / 60)
    pydirectinput.keyUp("c")


def dash():
    pydirectinput.keyDown("x")
    time.sleep(1 / 60)
    pydirectinput.keyUp("x")


def grab():
    pydirectinput.keyDown("z")


def unGrab():
    pydirectinput.keyUp("z")

def reset():
    pydirectinput.press('f8')