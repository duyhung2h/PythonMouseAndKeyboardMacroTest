
import os
import keyboard
from threading import *
import string


class KeyInput():
    def exit_listener():

        keys = list(string.ascii_lowercase)
        keys.append("space_bar")
        keys.append("backspace")
        keys.append("shift")
        keys.append("esc")
        """
        Optional code(extra keys):

        keys.append("space_bar")
        keys.append("backspace")
        keys.append("shift")
        keys.append("esc")
        """

        def listen(key):
            while True:
                keyboard.wait(key)
                print("[+] Pressed", key)
                if (key == "esc"):
                    os._exit(1)

        threads = [Thread(target=listen, kwargs={"key": key}) for key in keys]
        for thread in threads:
            thread.start()
