import time


from macro_functions.test import Test
from macro_functions.export_to_list import ExportToList
from macro_functions.JSON_to_pylist import JSONToPyList
from exit_functions.key_input import KeyInput

time.sleep(0.9)
KeyInput.exit_listener()
# ~~~~TEST FUNCTIONS~~~
# import pyautogui
# while True:
#     x, y = pyautogui.position()
#     px = pyautogui.pixel(x, y)
#     print(px) # (240, 240, 240)
# ~~~~~~~~~~~~~~~~~~~~~~~~
# from PIL import ImageGrab
#
# while True:
#     px = ImageGrab.grab().load()
#     color = px[350, 390]
#     print(color)
#     time.sleep(0.02)
# ~~~~~~~~~~~~~~~~~~~~~~~~
# import pyscreenshot
# while True:
#     getPic = pyscreenshot.grab().load() ## line 43
#     color = getPic[350, 390]
#     print(color)
#     time.sleep(0.02)





# ~~~~~~PRESS "ESC" TO EXIT THIS PROGRAM~~~~~~
# Test.start()

# ~~~~~~~~~~~~~~
export_to_list = ExportToList()
export_to_list.start()
# ~~~~~~~~~~~~~~
# JSONToPyList.start()
