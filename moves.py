import pydirectinput
import pyautogui
import time


def initialize():
    windows = pyautogui.getWindowsWithTitle('Celeste')
    for window in windows:
        if window.title == 'Celeste':
            window.maximize()



def moveRight(sleep_time):
    pydirectinput.keyDown("right")
    time.sleep(sleep_time)
    pydirectinput.keyUp("right")


def moveLeft(sleep_time):
    pydirectinput.keyDown("left")
    time.sleep(sleep_time)
    pydirectinput.keyUp("left")


def moveUp(sleep_time):
    pydirectinput.keyDown("up")
    time.sleep(sleep_time)
    pydirectinput.keyUp("up")


def moveDown(sleep_time):
    pydirectinput.keyDown("down")
    time.sleep(sleep_time)
    pydirectinput.keyUp("down")


def jump():
    pydirectinput.keyDown("c")
    time.sleep(1 / 60)
    pydirectinput.keyUp("c")

def longJump():
    pydirectinput.keyDown("c")
    time.sleep(10 / 60)
    pydirectinput.keyUp("c")


def dash(direction):
    match direction:
        case "up":
            pydirectinput.keyDown("up")
        case "up-left":
            pydirectinput.keyDown("up")
            pydirectinput.keyDown("left")
        case "left":
            pydirectinput.keyDown("left")
        case "down-left":
            pydirectinput.keyDown("down")
            pydirectinput.keyDown("left")
        case "down":
            pydirectinput.keyDown("down")
        case "down-right":
            pydirectinput.keyDown("down")
            pydirectinput.keyDown("right")
        case "right":
            pydirectinput.keyDown("right")
        case "up-right":
            pydirectinput.keyDown("up")
            pydirectinput.keyDown("right")
    pydirectinput.keyDown("x")
    time.sleep(1 / 60)
    pydirectinput.keyUp("x")
    pydirectinput.keyUp("up")
    pydirectinput.keyUp("left")
    pydirectinput.keyUp("down")
    pydirectinput.keyUp("right")


def grab():
    pydirectinput.keyDown("z")


def unGrab():
    pydirectinput.keyUp("z")
