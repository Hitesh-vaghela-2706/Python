import pyautogui as pg
import time

print("Program Will Run in 5 Second")
time.sleep(5)

for i in range(100):
    pg.write(f"Hitesh{i}")
    time.sleep(0.5)
    pg.press("Enter")
