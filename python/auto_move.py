import pyautogui

while(1):
    x,y = pyautogui.position()
    pyautogui.moveTo(x+100,y+100, duration=0.5)
    pyautogui.moveTo(x,y, duration=0.5)