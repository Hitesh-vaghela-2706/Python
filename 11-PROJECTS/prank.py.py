import pyautogui
import time
time.sleep(1)
print('hi')
text = 'ye to bokhla gaya re baba...'
X = 1
while True:
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    X += 1
    if (X>=4000):
        break