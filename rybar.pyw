#! python3
try:
    import pyautogui as pg
    import time as t
    import pydirectinput as pd
    import random
    import sys
    from pynput import mouse
    from PIL import Image
except:
    print("pip install pyautogui pynput pillow pydirectinput")
    exit()
def on_click(x, y, button, pressed):
    global cerv
    global bublinka
    if button == mouse.Button.left:
        return True
    if pressed:
        if cerv == (-1,-1):
            cerv = (x,y)
            print("Červ nastaven")
        else:
            bublinka = (x,y)
            print("Bublinka nastavena")
    else:
        return False

print("Klikni pravým na červa a pak klikni pravým na bublinku (tam kde je BÍLÁ)")
for _ in range(2):
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def nahodit():
    print("Nahazuju")
    pg.moveTo(x=bublinka[0], y=bublinka[1])
    t.sleep(0.3)
    pg.click(button="right")
    pg.moveTo(x=cerv[0], y=cerv[1])
    t.sleep(0.3)
    pg.click(button="right")
    t.sleep(0.3)
    pd.press(["space"])

cerv = (-1,-1)
bublinka = (-1,-1)
while True:
    nahodit()
    screen = pg.screenshot()
    start = t.time()
    while True:
        if t.time() >= start+60:
            print("Minuta uběhla, restartuju!")
            t.sleep(4)
            start = t.time()
            nahodit()
            screen = pg.screenshot()
        hledam = True
        for xRange in range(bublinka[0]-4, bublinka[0]+5):
            for yRange in range(bublinka[1]-4, bublinka[1]+5):
                if screen.getpixel((xRange, yRange)) >= (200,200,200):
                    print("Bublinka!")
                    hledam = False
                    break
            if not hledam:
                break
        if not hledam:
            break
        t.sleep(.3)
        screen = pg.screenshot()
    pg.moveTo(x=bublinka[0], y=bublinka[1])
    t.sleep(0.03)
    pg.click(button="right")
    t.sleep(72*0.03)
    pd.press(["space"])
    r = 3.75
    print(f"Čekám {r}s!")
    t.sleep(r)
    print("Jdu na to!")
