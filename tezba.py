#! python3
try:
    import pyautogui as pg
    import time as t
    import pydirectinput as pd
    import random, sys
    import multiprocessing as mp
    from pynput import mouse
    from PIL import Image
except Exception as e:
    print(e)
    print("pip install pyautogui pynput pillow pydirectinput")
    exit()
    
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        return True
    if pressed:
        souradnice.append((x,y))
    else:
        return False

def tezit(ruda):
    pg.moveTo(x=ruda[0], y=ruda[1])
    t.sleep(0.3)
    pg.click(button="right")
    t.sleep(0.3)
    pd.press(["x"])
    t.sleep(0.3)
    pg.click(button="left")

def mainLoop(ruda, chat, user, mutex):
    while True:
        with mutex:
            print(f"\33[2K\r{user=}: Tezit!\r", end="")
            tezit(ruda)
        print(f"\33[2K\r{user=}: Ignoruju Chat!\r", end="")
        t.sleep(10)
        hledam=True
        while True:
            screen = pg.screenshot()
            for xRange in range(chat[0]-4, chat[0]+5):
                for yRange in range(chat[1]-20, chat[1]):
                    if (screen.getpixel((xRange, yRange))) == (0xff,0xc8,0xc8):
                        print(f"\33[2K\r{user=}: Chat!\r", end="")
                        hledam = False
                        break
                if not hledam:
                    break
            if not hledam:
                break

if __name__ == "__main__":
    souradnice = []
    multiplier = int(sys.argv[1] if len(sys.argv)>1 else 1)
    print(f"{multiplier} uctu")
    print("Klikni pravým na rudu a pak klikni pravým na chat")
    for _ in range(2*multiplier):
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    mutex = mp.Lock()
    procesy = []
    for i in range(0, multiplier*2, 2):
        procesy.append(mp.Process(target=mainLoop, args=(souradnice[i], souradnice[i+1], i//2, mutex)))

    for p in procesy:
        p.start()
