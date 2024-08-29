import pyautogui as py
import time
import pyperclip
import keyboard
import numpy as np
import cv2



def go_to_page(page):
    n = page - 5 
    q, r = n // 2, n % 2
    print(n)
    print(q)
    print(r)
    if page >= 5:
        py.click(1533, 1330)
        if r == 1 and q > 0:
                for _ in range(q + 1):
                     py.click(1533, 1330)
                     time.sleep(4.5)
                py.click(1566, 1335)
                time.sleep(3.5)
        else:
             for _ in range(q + 1):
                        py.click(1533, 1330)
                        time.sleep(4.5)
    else:
        for _ in range(page):
              py.click(1566, 1335)
              time.sleep(4.5)
    

go_to_page(16)