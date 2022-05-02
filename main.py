import time


from macro_functions.test import Test
from macro_functions.export_to_list import ExportToList
from macro_functions.JSON_to_pylist import JSONToPyList
from exit_functions.key_input import KeyInput

time.sleep(0.9)
KeyInput.exit_listener()
# ~~~~TEST FUNCTIONS~~~
import pyautogui
while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    print(px) # (240, 240, 240)


# Test.start()

# ~~~~~~~~~~~~~~
export_to_list = ExportToList()
export_to_list.start()
# ~~~~~~~~~~~~~~
# JSONToPyList.start()
