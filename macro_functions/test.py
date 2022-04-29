import mouse
import keyboard
import time


class Test():
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def start():
        initial_val = 500001
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        # click first item
        mouse.move(100, 265, absolute=True, duration=.2)
        mouse.click("left")
        # move down a notch
        mouse.move(200, 580, absolute=True, duration=.2)
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        # shift click select all
        mouse.move(100, 660, absolute=True, duration=.2)
        keyboard.press("shift")
        mouse.click("left")
        keyboard.release("shift")
        # select language file name box
        mouse.move(260, 300, absolute=True, duration=.1)
        mouse.double_click("left")
        # fill with initial value
        keyboard.write(str(initial_val))
        keyboard.press("enter")
        keyboard.release("enter")
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        mouse.double_click("left")
        # keyboard.wait('enter')
        # fill first page
        for i in range(1, 31, 1):
            # do shit
            mouse.move(100, 251.5
                       + 1*13.3                       # + i*13.3
                       , absolute=True, duration=.01)
            # keyboard.wait('enter')
            keyboard.press("ctrl")
            mouse.click("left")
            keyboard.release("ctrl")
            # time.sleep(0.9)
            # select language file name box
            mouse.move(260, 300, absolute=True, duration=.01)
            mouse.double_click("left")
            # fill with initial value
            keyboard.write(str(initial_val + i))
            keyboard.press("enter")
            keyboard.release("enter")
        # Shift the page up again to start amend at the bottom
        mouse.move(200, 263, absolute=True, duration=.02)
        for i in range(1, 31, 1):
            mouse.double_click("left")
