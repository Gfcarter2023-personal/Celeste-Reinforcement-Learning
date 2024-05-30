import numpy as np
import pickle
import pyautogui
from jproperties import Properties
import math
import time

class State:
    def __init__(self, location):
        self.location = location

    def locate(self):
        return self.location

    def updateLocation(self):
        im1 = pyautogui.screenshot()
        im1.save("assets/screen.png")
        self.location = pyautogui.locateOnScreen("assets/Celeste.png", im1, confidence=0.55)

    def celesteToPCCoordinates(self, x, y):
        configs = Properties()
        with open('properties.txt', 'rb') as read_prop:
            configs.load(read_prop)
        left = (x * float(configs.get("x-scale").data)) + float(configs.get("x-offset").data)
        top = (y * float(configs.get("y-scale").data)) + float(configs.get("y-offset").data)
        return left, top

    def isAllowedAction(self, action):
        return True

    def giveReward(self):
        configs = Properties()
        with open('LocationRewards/room1.txt', 'rb') as read_prop:
            configs.load(read_prop)
        rewardVal = 0
        prop_view = configs.items()
        self.updateLocation()
        playerCoordinate = self.locate()
        for rewards in prop_view:
            xStr, yStr = rewards[1].data.split()
            x, y = self.celesteToPCCoordinates(int(xStr), int(yStr))
            pyautogui.moveTo(x,y)
            rewardDistance = math.sqrt((int(x) - playerCoordinate[0])**2 + (int(y) - playerCoordinate[1])**2)
            rewardVal += float(rewards[0])**4 / float(rewardDistance)
        print(rewardVal)
        return rewardVal
