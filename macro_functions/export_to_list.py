import mouse
import keyboard
import pyautogui
import time
from tkinter import Tk
import json
import pyscreenshot
from screen_location.screen_location_data import ScreenLocationData
import gc

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
        self.sleep_time = 0.001
        # self.sleep_time = 1
    def get_file_name(self):
        if copy_from_field == TF_LANGUAGE_FILENAME:
            file_name = "JSON_old.json"
            # file_name = "JSON_new.json"
        elif copy_from_field == TF_INTERNAL_UNIT_NAME:
            file_name = "JSON_iuname_old.json"
            # file_name = "JSON_iuname_new.json"
        return file_name

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
        time.sleep(self.sleep_time)

    def insert_to_json_file(self, item):
        # write insert one item to JSON file item list at the end here
        # select copy textfield box
        file_name = self.get_file_name()
        with open("exported_JSON/" + file_name, "a+") as feedsjson:
            feeds = []
            try:
                feeds = json.load(feedsjson)
            except:
                feeds = []
            feeds.append(item)
            json.dump(item, feedsjson)
            if self.amount_to_update > self.current_index + 1:
                feedsjson.write(',')
            feedsjson.write('\n')
            keyboard.press('backspace')
            time.sleep(self.sleep_time*1000)
            del file_name
            del feeds
            del feedsjson
            del item
            gc.collect()

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
                    # print(m)
                    # select copy textfield box
                    if copy_from_field == TF_LANGUAGE_FILENAME:
                        mouse.move(self.location.name_box.x,
                                   self.location.name_box.y, absolute=True, duration=self.sleep_time)
                    elif copy_from_field == TF_INTERNAL_UNIT_NAME:
                        mouse.move(self.location.iu_name_box.x,
                                   self.location.iu_name_box.y, absolute=True, duration=self.sleep_time)
                    # print(str(Tk().clipboard_get()) + "(clipboard) " + str(m) + "(color) " +
                    #       str(self.current_index) + "(currentIndex) ")  # (240, 240, 240)
                    while str(Tk().clipboard_get()) == '1000000' and m == (215, 255, 255):
                        mouse.click("left")
                        time.sleep(self.sleep_time)
                        keyboard.press('space')
                        time.sleep(self.sleep_time)
                        keyboard.release('space')
                        time.sleep(self.sleep_time)
                        keyboard.press('1')
                        time.sleep(self.sleep_time)
                        keyboard.release('1')
                        time.sleep(self.sleep_time)
                        mouse.click("left")
                        # mouse.click("left")
                        time.sleep(self.sleep_time)
                        keyboard.press('ctrl+x')
                        time.sleep(self.sleep_time)
                        keyboard.release('ctrl+x')
                        time.sleep(self.sleep_time)
                        keyboard.press('backspace')
                        time.sleep(self.sleep_time*10)
                        keyboard.release('backspace')
                        time.sleep(self.sleep_time*1000)
                        # keyboard.press('backspace')
                        # keyboard.release('backspace')
                        # time.sleep(self.sleep_time*100)
                        # time.sleep(self.sleep_time*10000000000)
                    while str(Tk().clipboard_get()) == '1' and m == (215, 255, 255):
                        keyboard.press('ctrl+a')
                        keyboard.release('ctrl+a')
                        time.sleep(self.sleep_time)
                        keyboard.press('ctrl+c')
                        keyboard.release('ctrl+c')
                        time.sleep(self.sleep_time)
                        mouse.click("left")
                        time.sleep(self.sleep_time)
                        keyboard.press('left')
                        time.sleep(self.sleep_time)
                        keyboard.release('left')
                        time.sleep(self.sleep_time)
                        keyboard.press('space')
                        time.sleep(self.sleep_time*10)
                        keyboard.release('space')
                    # append to JSON
                    item = {}
                    if copy_from_field == TF_LANGUAGE_FILENAME:
                        item = {str(self.current_index)
                                    : int(Tk().clipboard_get())}
                    elif copy_from_field == TF_INTERNAL_UNIT_NAME:
                        item = {str(self.current_index)
                                    : str(Tk().clipboard_get())}
                    self.insert_to_json_file(item)
                    # garbage collection
                    del number_of_tries
                    del item
                    del screen
                    del px
                    del m
                    gc.collect()
                    break
                else:
                    # print("fill 1000000")
                    self.fill_dummy_value("1000000")
                    number_of_tries = number_of_tries + 1
            except Exception as ex:
                time.sleep(1.000)
                print(ex)
                print("index " + str(self.current_index) + ": rescanning...")
                self.fill_dummy_value("1000000")
                number_of_tries = 0

    def start(self):
        # select copy textfield box
        file_name = self.get_file_name()
        f = open("exported_JSON/" + file_name, "a")
        f.truncate(0)
        f.write('{\n"items": [\n')
        f.close()
        # test
        # mouse.move(10, 10, absolute=True, duration=.2)
        # mouse.move(self.location.scroll_top.x, self.location.scroll_top.y, absolute=False, duration=.2)
        # keyboard.wait("capslock")   #TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-TEST-
        # ~~~~start

        # move up a notch
        mouse.move(self.location.scroll_top.x,
                   self.location.scroll_top.y, absolute=True, duration=self.sleep_time)
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # click first item
        mouse.move(self.location.first_item.x,
                   self.location.first_item.y, absolute=True, duration=self.sleep_time)
        mouse.click("left")
        for i in range(0, 60, 1):
            mouse.double_click("left")
        # fill first page
        for i in range(0, 30, 1):
            # do shit
            # copy found value to List
            mouse.move(self.location.first_item.x, self.location.first_item.y
                       + i*self.location.row_length, absolute=True, duration=self.sleep_time)
            mouse.click("left")
            self.get_name_value()
            self.current_index = self.current_index + 1
            # -----------------------

        # Shift the page up again to start amend at the bottom
        mouse.move(self.location.scroll_top.x,
                   self.location.scroll_top.y, absolute=True, duration=self.sleep_time*2)
        for i in range(0, 30, 1):
            mouse.double_click("left")
        for i in range(0, 30, 1):
            mouse.double_click("left")
            # self.amount_to_update = self.amount_to_update - 1
        # click down 1 item
        for i in range(30, self.amount_to_update, 1):
            mouse.move(self.location.last_item.x,
                       self.location.last_item.y, absolute=True, duration=self.sleep_time)
            mouse.click("left")
            time.sleep(self.sleep_time)
            # mouse.move(self.location.last_item.x,
            #            self.location.last_item.y + 10, absolute=True, duration=self.sleep_time)
            # mouse.click("left")
            # time.sleep(self.sleep_time*100)
            # copy found value to List
            self.get_name_value()
            self.current_index = self.current_index + 1
            # -----------------------

        # Write closing statements
        file_name = self.get_file_name()
        f = open("exported_JSON/" + file_name, "a")
        f.truncate(self.get_size(f) - 1)
        f.write("\n]\n}")
        f.close()
        print('done!')

    def get_size(self, fileobject):
        fileobject.seek(0,2) # move the cursor to the end of the file
        size = fileobject.tell()
        return size