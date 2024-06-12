import os

import numpy as np
import pickle
import pyautogui
from jproperties import Properties
import math
import time
import cv2

class State:
    def __init__(self, location=(0,0)):
        self.location = location

    def locate(self):
        return self.location

    def findLocation(self, oldLocation=(-1, -1, -1, -1)):
        try:
            if oldLocation == (-1, -1, -1, -1):
                self.location = pyautogui.locateOnScreen("assets/Celeste.png", confidence=0.60)
            else:
                im = pyautogui.screenshot("assets/screen.png", region=(int(oldLocation[0] - 400), int(oldLocation[1] - 400), 800, 800))
                self.location = pyautogui.locateOnScreen("assets/Celeste.png", confidence=0.60, region=(int(oldLocation[0] - 400), int(oldLocation[1] - 400), 800, 800))
        except pyautogui.ImageNotFoundException:
            self.location = (-1, -1, -1, -1)




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
        self.findLocation()
        print(self.location)
        playerCoordinate = self.locate()
        if playerCoordinate[0] < 0:
            return -1
        else:
            for rewards in prop_view:
                xStr, yStr = rewards[1].data.split()
                x, y = self.celesteToPCCoordinates(int(xStr), int(yStr))
                rewardDistance = math.sqrt((int(x) - playerCoordinate[0]) ** 2 + (int(y) - playerCoordinate[1]) ** 2)
                rewardVal += 100 * float(rewards[0])/ float(rewardDistance)
            return rewardVal

