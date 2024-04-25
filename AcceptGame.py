import pyautogui
import os
def GetImagePaths():
    ImagePaths = []
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    imageDirectory = os.path.join(currentDirectory, "Images")
    for Image in os.listdir(imageDirectory):
        if Image.endswith(".png"):
            ImagePaths.append(os.path.join(imageDirectory, Image))
    return ImagePaths

def Capture():
    return pyautogui.screenshot()

def SearchImage(Screenshot, Image):
    try:
        Location = pyautogui.locateCenterOnScreen(Image, confidence=0.5, region=(0 , 0, Screenshot.width, Screenshot.height))
    except:
        Location = None
    return Location

def AcceptGame():
    ImagePaths = GetImagePaths()
    while True:
        Screenshot = Capture()
        for Image in ImagePaths:
            AcceptButton = SearchImage(Screenshot, Image)
            if AcceptButton:
                pyautogui.click(AcceptButton)
                return

def main():
    AcceptGame()
    print("Game Accepted")
    return 0
main()