import os

import numpy as np
import pickle
import pyautogui
from jproperties import Properties
import math
import time
import cv2

class State:
    def __init__(self, location):
        self.location = location

    def locate(self):
        return self.location

    def findLocation(self):
        self.location = pyautogui.locateOnScreen("assets/Celeste.png", confidence=0.60)

    def updateLocation(self, old_loc=None):
        im1 = pyautogui.screenshot()
        im1 = cv2.cvtColor(np.array(im1), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        best_confidence = 0
        best_location = None
        for images in os.listdir('assets/CelesteModel'):
            image = cv2.imread('assets/CelesteModel/' + images, cv2.IMREAD_GRAYSCALE)
            result = cv2.matchTemplate(screenshot_gray, image, cv2.TM_CCOEFF_NORMED)
            # Get the best match position and confidence
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # Check if this is the best match so far
            if max_val > best_confidence:
                best_confidence = max_val
                best_location = max_loc
        print(best_location)
        self.location = best_location


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
        pyautogui.moveTo(playerCoordinate)
        for rewards in prop_view:
            xStr, yStr = rewards[1].data.split()
            x, y = self.celesteToPCCoordinates(int(xStr), int(yStr))
            rewardDistance = math.sqrt((int(x) - playerCoordinate[0])**2 + (int(y) - playerCoordinate[1])**2)
            rewardVal += float(rewards[0])**4 / float(rewardDistance)
        print(rewardVal)
        return rewardVal
