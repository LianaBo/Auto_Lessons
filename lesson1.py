import pyautogui as pg
import time
import os


file = "GoodFile.txt"
path = "C:\\Users\\User\\Desktop\\Python\\" + file

if os.path.exists(file):
    os.remove(file)

pg.hotkey("winleft")
time.sleep(2)
pg.typewrite("notepad\n", 0.9)
time.sleep(1)

expect = "Good job"
pg.typewrite(expect, 0.1)
pg.hotkey("ctrl", "s")
time.sleep(1)

pg.typewrite(path + "\n", 0.1)

actual = ""
with open(path) as inf:
    actual = inf.readline()

if actual == expect:
    print("Passed")
else:
    print("Failed")

pg.hotkey("alt","F4")




