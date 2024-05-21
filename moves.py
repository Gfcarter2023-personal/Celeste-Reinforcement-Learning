import pyautogui
import time


def initialize():
    windows = pyautogui.getWindowsWithTitle('Celeste')
    for window in windows:
        if window.title == 'Celeste':
            window.activate()


def moveRight(sleep_time):
    pyautogui.keyDown("right")
    time.sleep(sleep_time)
    pyautogui.keyUp("right")


def moveLeft(sleep_time):
    pyautogui.keyDown("left")
    time.sleep(sleep_time)
    pyautogui.keyUp("left")


def moveUp(sleep_time):
    pyautogui.keyDown("up")
    time.sleep(sleep_time)
    pyautogui.keyUp("up")


def moveDown(sleep_time):
    pyautogui.keyDown("down")
    time.sleep(sleep_time)
    pyautogui.keyUp("down")


def jump():
    pyautogui.keyDown("c")
    time.sleep(0.1)
    pyautogui.keyUp("c")

def dash():
    pyautogui.keyDown("x")
    time.sleep(1 / 60)
    pyautogui.keyUp("x")

def dashDirection(direction):
    match direction:
        case "up":
            pyautogui.keyDown("up")
        case "up-left":
            pyautogui.keyDown("up")
            pyautogui.keyDown("left")
        case "left":
            pyautogui.keyDown("left")
        case "down-left":
            pyautogui.keyDown("down")
            pyautogui.keyDown("left")
        case "down":
            pyautogui.keyDown("down")
        case "down-right":
            pyautogui.keyDown("down")
            pyautogui.keyDown("right")
        case "right":
            pyautogui.keyDown("right")
        case "up-right":
            pyautogui.keyDown("up")
            pyautogui.keyDown("right")
            dash()
            pyautogui.keyUp("up")
            pyautogui.keyUp("left")
            pyautogui.keyUp("down")
            pyautogui.keyUp("right")





def grab():
    return True


