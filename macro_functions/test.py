import keyboard
import mouse


class Test():
    def __init__(self):
        self = self

    def start():
        initial_val = 500001
        updating_val = int(initial_val)
        amount_to_update = 117 + (1)
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # click first item
        mouse.move(100, 265, absolute=True, duration=.2)
        mouse.click("left")
        # move down a notch
        mouse.move(200, 580, absolute=True, duration=.2)
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
        # fill with initial value
        keyboard.write(str(initial_val))
        keyboard.press("enter")
        keyboard.release("enter")
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # keyboard.wait('enter')
        # fill first page
        updating_val = updating_val + 1
        for i in range(0, 31, 1):
            # do shit
            mouse.move(100, 251.5
                       + 1 * 13.3  # + i*13.3
                       , absolute=True, duration=.001)
            # keyboard.wait('enter')
            keyboard.press("ctrl")
            mouse.click("left")
            keyboard.release("ctrl")
            # time.sleep(0.9)
            # select language file name box
            mouse.move(260, 300, absolute=True, duration=.001)
            mouse.double_click("left")
            # fill with initial value
            keyboard.write(str(updating_val))
            updating_val = updating_val + 1
            keyboard.press("enter")
            keyboard.release("enter")
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
            # fill with initial value
            keyboard.write(str(updating_val))
            updating_val = updating_val + 1
            # keyboard.press("enter")
            # keyboard.release("enter")
