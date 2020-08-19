#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
import math
import untitled_ui as ui


class ComputeArea(QWidget, ui.Ui_Form):
    SQUARE, CIRCLE = 0, 1

    def __init__(self):
        super(ComputeArea, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('ComputeArea')
        self.gb_circle.setVisible(False)
        self.setFixedSize(290, 180)

        self.sb_radius.valueChanged.connect(self.compute)
        self.sb_height.valueChanged.connect(self.compute)
        self.sb_width.valueChanged.connect(self.compute)
        self.cb_select_shape.currentIndexChanged.connect(self.group_box_visible)

    def compute(self):
        combo_box_index = self.cb_select_shape.currentIndex()

        if combo_box_index == self.SQUARE:
            height = self.sb_height.value()
            width = self.sb_width.value()
            area = height * width
        elif combo_box_index == self.CIRCLE:
            r = self.sb_radius.value()
            area = round(math.pi * r ** 2, 3)
        self.result_text(area)

    def result_text(self, text):
        self.lb_result.setText("Result: " + str(text))

    def group_box_visible(self, index):
        if index == self.CIRCLE:
            self.gb_circle.setVisible(True)
            self.gb_square.setVisible(False)
        elif index == self.SQUARE:
            self.gb_circle.setVisible(False)
            self.gb_square.setVisible(True)
        self.compute()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ComputeArea()
    win.show()
    sys.exit(app.exec_())
