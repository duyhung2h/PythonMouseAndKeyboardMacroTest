class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ScreenLocationData:

    def __init__(self):
        # add 50, 75

        self.color_check = XY(350, 390)
        '''
        # Scroll
        self.scroll_top = XY(250, 345)
        self.scroll_bottom = XY(250, 820)
        # item
        self.first_item = XY(150, 335)
        self.last_item = XY(150, 830)
        # textbox
        self.name_box = XY(350, 375)
        self.dump_box = XY(350, 740)
        # item row length
        self.row_length = 17
        '''

        # old value
        # Scroll
        self.scroll_top = XY(200, 275)
        self.scroll_bottom = XY(200, 656)
        # item
        self.first_item = XY(100, 265)
        self.last_item = XY(100, 660)
        # textbox
        self.name_box = XY(260, 310)
        self.dump_box = XY(260, 580)
        # item row length
        self.row_length = 13.5