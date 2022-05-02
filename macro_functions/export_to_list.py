import mouse
import keyboard
import time
from tkinter import Tk
import json


class ExportToList():
    def __init__(self):
        self.amount_to_update = 1800 + (1)
        self.current_index = 0
        self.name_list = []

    def fill_dummy_value(self, value):
        mouse.move(260, 570, absolute=True, duration=.001)
        # keyboard.wait('shift')
        mouse.double_click("left")
        keyboard.write(value)
        mouse.double_click("left")
        keyboard.press('ctrl+c')
        keyboard.release('ctrl+c')
        time.sleep(0.000)

    def get_name_value(self):
        # copy found value to List
        number_of_tries = 0
        while True:
            try:
                self.fill_dummy_value(" ")
                if str(Tk().clipboard_get()) == ' ':
                    # ~~~~
                    # select language file name box
                    if number_of_tries > 10:
                        mouse.move(260, 300, absolute=True, duration=.001)
                        mouse.double_click("left")
                        time.sleep(0.000)
                        keyboard.press('ctrl+c')
                        keyboard.release('ctrl+c')
                        time.sleep(0.000)
                        self.name_list.append(
                            {str(self.current_index): int(Tk().clipboard_get())})
                        # print(str(self.current_index) + ": ", str(Tk().clipboard_get()))
                        break
                    else:
                        self.fill_dummy_value("1000000")
                        number_of_tries = number_of_tries + 1
            except:
                print("index " + str(self.current_index) + ": rescanning...")

    def start(self):
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # click first item
        mouse.move(100, 265, absolute=True, duration=.2)
        mouse.click("left")
        # move down a notch
        mouse.move(200, 655, absolute=True, duration=.2)
        for i in range(0, 31, 1):
            mouse.double_click("left")
        # shift click select all
        mouse.move(100, 663.5, absolute=True, duration=.2)
        keyboard.press("shift")
        mouse.click("left")
        keyboard.release("shift")
        # select language file name box
        mouse.move(260, 300, absolute=True, duration=.1)
        mouse.double_click("left")
        # move up a notch
        mouse.move(200, 275, absolute=True, duration=.2)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # fill first page
        # self.fill_dummy_value(" ")
        for i in range(0, 30, 1):
            # do shit
            mouse.move(100, 250
                       # + 1*13.3
                       + i*13.5, absolute=True, duration=.001)
            # keyboard.wait('shift')
            keyboard.press("ctrl")
            mouse.click("left")
            keyboard.release("ctrl")
            # copy found value to List
            self.get_name_value()
            self.current_index = self.current_index + 1
            # -----------------------

        # Shift the page up again to start amend at the bottom
        mouse.move(200, 263, absolute=True, duration=.002)
        for i in range(0, 30, 1):
            mouse.double_click("left")
            self.amount_to_update = self.amount_to_update - 1
        # click down 1 item
        for i in range(0, self.amount_to_update, 1):
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
            self.get_name_value()
            self.current_index = self.current_index + 1
            # -----------------------

        print('done!')
        # write to JSON file!
        jsonStr = json.dumps({'items': self.name_list})
        # f = open("exported_JSON/JSON_old.json", "a")
        f = open("exported_JSON/JSON_new.json", "a")
        f.truncate(0)
        f.write(jsonStr)
        f.close()
