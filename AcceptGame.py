import pyautogui
import time
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))

ImagePath = os.path.join(currentDirectory, 'Images', 'AcceptButton.png')


def Capture():
    Screenshot = pyautogui.screenshot()

    return Screenshot

def SearchImage(Screenshot, Image):
    try:
        Location = pyautogui.locateCenterOnScreen(Image, confidence=0.9, region=(0, 0, Screenshot.width, Screenshot.height))
    except:
        Location = None

    return Location

def AcceptGame():
    condition = True

    while condition:
        Screenshot = Capture()
        AcceptButton = SearchImage(Screenshot, ImagePath)

        if AcceptButton:
            pyautogui.click(AcceptButton)
            condition = False
        else:
            time.sleep(1)

def main():
    AcceptGame()

    print("Game Accepted")

    return 0

main()
