import json
import time
import pyscreenshot
import mouse
import keyboard
from tkinter import Tk
from screen_location.screen_location_data import ScreenLocationData


class JSONToPyList():
    def __init__(self):
        self = self
        self.name_list = []
        self.location = ScreenLocationData()

    def start(self):
        # Open existing JSON file!
        f = open("exported_JSON/perfected JSON/JSON_modded_DOTD.json", "r")
        jsonStr = f.read()
        data = json.loads(jsonStr)
        name_list = data['items']

        f2 = open("exported_JSON/perfected JSON/JSON_vanilla_DOI.json", "r")
        jsonStr2 = f2.read()
        data2 = json.loads(jsonStr2)
        name_list2 = data2['items']
        # print(len(name_list))
        for i in range(0, len(name_list)-1, 1):
            # print(name_list2[i][str(i)])
            if name_list2[i][str(i)] == '0' or int(name_list[i][str(i)]) <= 499999:
                self.name_list.append(
                    {str(i): name_list2[i][str(i)]})
            elif int(name_list[i][str(i)]) > 499999:
                self.name_list.append(
                    {str(i): name_list[i][str(i)]})

        # write to JSON file!
        jsonStrEnd = json.dumps({'items': self.name_list})
        fEnd = open("exported_JSON/perfected JSON/JSON_modded_DOI.json", "a")
        # f = open("exported_JSON/JSON_new.json", "a")
        fEnd.truncate(0)
        fEnd.write(jsonStrEnd)
        fEnd.close()
        print('done!')

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

    def fetch_list_eachitem(self, item, index):
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
                          str(item) + "(item) "
                          + str(index) + "(currentIndex) "
                          + str(item[str(index)]) + "(value) "
                          )  # (240, 240, 240)
                    while str(Tk().clipboard_get()) == '1000000' and m == (215, 255, 255):
                        mouse.click("left")
                        time.sleep(0.000)
                        keyboard.press('ctrl+a')
                        keyboard.release('ctrl+a')
                        time.sleep(0.000)
                        keyboard.write(str(item[str(index)]))
                        mouse.click("left")
                        time.sleep(0.000)
                        keyboard.press('ctrl+a')
                        keyboard.release('ctrl+a')
                        time.sleep(0.000)
                        keyboard.press('ctrl+c')
                        keyboard.release('ctrl+c')
                        time.sleep(0.000)
                    break
                else:
                    print("fill 1000000")
                    self.fill_dummy_value("1000000")
                    number_of_tries = number_of_tries + 1
            except Exception as ex:
                time.sleep(1.000)
                print(ex)
                print("index " + str(item) + ": rescanning...")
                self.fill_dummy_value("1000000")
                number_of_tries = 0

    def fetch_list(self):
        f = open("exported_JSON/perfected JSON/JSON_modded_DOI.json", "r")
        jsonStr = f.read()
        data = json.loads(jsonStr)
        name_list = data['items']
        # lets get started - initial setup
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
        # fill first page
        for i in range(0, 30, 1):
            # do shit
            # copy found value to List
            mouse.move(self.location.first_item.x, self.location.first_item.y
                       + i*self.location.row_length, absolute=True, duration=.001)
            mouse.click("left")
            self.fetch_list_eachitem(name_list[i], i)
            # -----------------------
        # goes one by one item in list
        for i in range(30, len(name_list)-1, 1):
            mouse.move(self.location.last_item.x,
                       self.location.last_item.y - 5, absolute=True, duration=.002)
            mouse.click("left")
            mouse.move(self.location.last_item.x,
                       self.location.last_item.y + 10, absolute=True, duration=.002)
            mouse.click("left")
            self.fetch_list_eachitem(name_list[i], i)
