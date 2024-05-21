import pyautogui
import time


def initialize():
    pyautogui.getWindowsWithTitle('Celeste')[0].activate()

def moveLeft(sleep_time):
    pyautogui.keyDown("left")
    time.sleep(sleep_time)
    pyautogui.keyUp("left")

def moveRight(sleep_time):
    pyautogui.keyDown("right")
    time.sleep(sleep_time)
    pyautogui.keyUp("right")


def moveUp(sleep_time):
    pyautogui.keyDown("up")
    time.sleep(sleep_time)
    pyautogui.keyUp("up")


def moveDown(sleep_time):
    pyautogui.keyDown("down")
    time.sleep(sleep_time)
    pyautogui.keyUp("down")


def jump():
    pyautogui.press('c')


def dash():
    pyautogui.press('x')


def grab():
    return True


def moveLeft():
    return True


def moveLeft():
    return True


def moveLeft():
    return True


def moveLeft():
    return True


def moveLeft():
    return True
