import mouse
import keyboard
import time
import win32clipboard
from tkinter import Tk


class ExportToList():
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def start():
        initial_val = 500001
        updating_val = int(initial_val)
        amount_to_update = 20 + (1)
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # click first item
        mouse.move(100, 265, absolute=True, duration=.2)
        mouse.click("left")
        # move down a notch
        mouse.move(200, 656, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # shift click select all
        mouse.move(100, 660, absolute=True, duration=.2)
        keyboard.press("shift")
        mouse.click("left")
        keyboard.release("shift")
        # select language file name box
        mouse.move(260, 300, absolute=True, duration=.1)
        mouse.double_click("left")
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # fill first page
        updating_val = updating_val + 1
        for i in range(0, 31, 1):
            # do shit
            mouse.move(100, 250
                       # + 1*13.3
                       + i*13.5
                       , absolute=True, duration=.001)
            # keyboard.wait('enter')
            keyboard.press("ctrl")
            mouse.click("left")
            keyboard.release("ctrl")
            # time.sleep(0.9)
            # select language file name box
            mouse.move(260, 300, absolute=True, duration=.001)
            mouse.double_click("left")
            # copy found value to List
            keyboard.press('ctrl+c')
            keyboard.release('ctrl+c')
            time.sleep(0.05)
            print(Tk().clipboard_get())
            # -----------------------
            updating_val = updating_val + 1
        # Shift the page up again to start amend at the bottom
        updating_val = updating_val - 2
        mouse.move(200, 263, absolute=True, duration=.002)
        for i in range(1, 32, 1):
            mouse.double_click("left")
            amount_to_update = amount_to_update - 1
        # click down 1 item
        for i in range(0, amount_to_update, 1):
            mouse.move(100, 664, absolute=True, duration=.002)
            # keyboard.wait('capslock') # wait
            mouse.click("left")
            mouse.move(100, 675, absolute=True, duration=.002)
            # keyboard.wait('capslock') # wait
            mouse.click("left")
            # select language file name box
            mouse.move(260, 300, absolute=True, duration=.003)
            # keyboard.wait('capslock') # wait
            mouse.double_click("left")
            # copy found value to List
            keyboard.press('ctrl+c')
            keyboard.release('ctrl+c')
            print(Tk().clipboard_get())
            # -----------------------
            updating_val = updating_val + 1


