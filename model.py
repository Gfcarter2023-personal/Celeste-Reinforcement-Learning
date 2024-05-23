import numpy as np
import pickle
import pyautogui
from jproperties import Properties


class State:
    def __init__(self, location):
        self.location = location

    def locate(self):
        return self.location

    def updateLocation(self):
        self.location = pyautogui.locateOnWindow("Celeste.png")

    def celesteCoordinates(self):
        configs = Properties()
        with open('properties.txt') as read_prop:
            configs.load(read_prop)
        left = (self.location[0] * configs.get("x-scale").data) + configs.get("x-offset").data
        top = (self.location[1] * configs.get("y-scale").data) + configs.get("y-offset").data
        return left, top, self.location[2], self.location[3]
