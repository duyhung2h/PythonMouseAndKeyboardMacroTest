import mouse
import keyboard
import time
from tkinter import Tk
import json
import pyscreenshot
from screen_location.screen_location_data import ScreenLocationData
# from PIL import ImageGrab

TF_LANGUAGE_FILENAME = 0
TF_INTERNAL_UNIT_NAME = 1
copy_from_field = TF_INTERNAL_UNIT_NAME

class ExportToList():
    def __init__(self):
        # 1800 units as of now
        # 278 to get to special area
        self.amount_to_update = 1800 + (1)
        self.current_index = 0
        self.name_list = []
        self.location = ScreenLocationData()

    def fill_dummy_value(self, value):
        mouse.move(self.location.dump_box.x,
                   self.location.dump_box.y, absolute=True, duration=.001)
        mouse.click("left")
        keyboard.press('ctrl+a')
        keyboard.release('ctrl+a')
        keyboard.write(value)
        keyboard.press('ctrl+a')
        keyboard.release('ctrl+a')
        keyboard.press('ctrl+c')
        keyboard.release('ctrl+c')
        time.sleep(0.000)

    def get_name_value(self):
        # copy found value to List
        number_of_tries = 0
        while True:
            try:
                # ~~~~
                if number_of_tries > 10 or str(Tk().clipboard_get()) == '1000000':
                    # select language file name box
                    screen = pyscreenshot.grab(bbox=(self.location.color_check.x, self.location.color_check.y,
                                            self.location.color_check.x+1, self.location.color_check.y+1))
                    px = screen.load()
                    m = px[0, 0]
                    print(m)
                    mouse.move(self.location.name_box.x,
                               self.location.name_box.y, absolute=True, duration=.000)
                    print(str(Tk().clipboard_get()) + "(clipboard) " + str(m) + "(color) " +
                          str(self.current_index) + "(currentIndex) ")  # (240, 240, 240)
                    while str(Tk().clipboard_get()) == '1000000' and m == (215, 255, 255):
                        mouse.click("left")
                        time.sleep(0.000)
                        keyboard.press('ctrl+a')
                        keyboard.release('ctrl+a')
                        time.sleep(0.000)
                        keyboard.press('ctrl+c')
                        keyboard.release('ctrl+c')
                        time.sleep(0.000)
                    self.name_list.append(
                        {str(self.current_index): int(Tk().clipboard_get())})
                    break
                else:
                    print("fill 1000000")
                    self.fill_dummy_value("1000000")
                    number_of_tries = number_of_tries + 1
            except Exception as ex:
                time.sleep(1.000)
                print(ex)
                print("index " + str(self.current_index) + ": rescanning...")
                self.fill_dummy_value("1000000")
                number_of_tries = 0

    def start(self):
        # test
        # mouse.move(10, 10, absolute=True, duration=.2)
        # mouse.move(self.location.scroll_top.x, self.location.scroll_top.y, absolute=False, duration=.2)
        # keyboard.wait("capslock")   #TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-
        # ~~~~start
        # move up a notch
        mouse.move(self.location.scroll_top.x,
                   self.location.scroll_top.y, absolute=True, duration=.2)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # click first item
        mouse.move(self.location.first_item.x,
                   self.location.first_item.y, absolute=True, duration=.2)
        mouse.click("left")
        # move down a notch
        mouse.move(self.location.scroll_bottom.x,
                   self.location.scroll_bottom.y, absolute=True, duration=.2)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # shift click select all
        mouse.move(self.location.last_item.x,
                   self.location.last_item.y, absolute=True, duration=.2)
        keyboard.press("shift")
        mouse.click("left")
        keyboard.release("shift")
        # select copy textfield box
        if copy_from_field == TF_LANGUAGE_FILENAME:
            mouse.move(self.location.name_box.x,
                       self.location.name_box.y, absolute=True, duration=.1)
        elif copy_from_field == TF_INTERNAL_UNIT_NAME:
            mouse.move(self.location.iu_name_box.x,
                       self.location.iu_name_box.y, absolute=True, duration=.1)
        # keyboard.wait("capslock")   #TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-
        mouse.click("left")
        time.sleep(0.000)
        keyboard.press('ctrl+a')
        keyboard.release('ctrl+a')
        # move up a notch
        mouse.move(self.location.scroll_top.x,
                   self.location.scroll_top.y, absolute=True, duration=.2)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # fill first page
        for i in range(0, 30, 1):
            # do shit
            # copy found value to List
            self.get_name_value()
            self.current_index = self.current_index + 1
            mouse.move(self.location.first_item.x, self.location.first_item.y
                       + i*self.location.row_length, absolute=True, duration=.001)
            keyboard.press("ctrl")
            mouse.click("left")
            keyboard.release("ctrl")
            # -----------------------

        # Shift the page up again to start amend at the bottom
        mouse.move(self.location.scroll_top.x,
                   self.location.scroll_top.y, absolute=True, duration=.002)
        for i in range(0, 30, 1):
            mouse.double_click("left")
        for i in range(0, 30, 1):
            mouse.double_click("left")
            self.amount_to_update = self.amount_to_update - 1
        # click down 1 item
        for i in range(0, self.amount_to_update, 1):
            mouse.move(self.location.last_item.x,
                       self.location.last_item.y - 5, absolute=True, duration=.002)
            mouse.click("left")
            mouse.move(self.location.last_item.x,
                       self.location.last_item.y + 10, absolute=True, duration=.002)
            mouse.click("left")
            # copy found value to List
            self.get_name_value()
            self.current_index = self.current_index + 1
            # -----------------------

        # write to JSON file!
        jsonStr = json.dumps({'items': self.name_list})
        # f = open()
        # select copy textfield box
        if copy_from_field == TF_LANGUAGE_FILENAME:
            f = open("exported_JSON/JSON_old.json", "a")
            # f = open("exported_JSON/JSON_new.json", "a")
        elif copy_from_field == TF_INTERNAL_UNIT_NAME:
            f = open("exported_JSON/JSON_iuname_old.json", "a")
            # f = open("exported_JSON/JSON_iuname_new.json", "a")
        f.truncate(0)
        f.write(jsonStr)
        f.close()
        print('done!')
