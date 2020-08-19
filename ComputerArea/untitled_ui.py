# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PPython\Project\pyQT\ComputerArea\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(293, 251)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_select_shape = QtWidgets.QComboBox(self.groupBox)
        self.cb_select_shape.setObjectName("cb_select_shape")
        self.cb_select_shape.addItem("")
        self.cb_select_shape.addItem("")
        self.verticalLayout.addWidget(self.cb_select_shape)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.gb_square = QtWidgets.QGroupBox(Form)
        self.gb_square.setObjectName("gb_square")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_square)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.gb_square)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sb_height = QtWidgets.QSpinBox(self.gb_square)
        self.sb_height.setMaximum(999999999)
        self.sb_height.setObjectName("sb_height")
        self.horizontalLayout.addWidget(self.sb_height)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gb_square)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sb_width = QtWidgets.QSpinBox(self.gb_square)
        self.sb_width.setMaximum(999999999)
        self.sb_width.setObjectName("sb_width")
        self.horizontalLayout_2.addWidget(self.sb_width)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.gb_square)
        self.gb_circle = QtWidgets.QGroupBox(Form)
        self.gb_circle.setObjectName("gb_circle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gb_circle)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gb_circle)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.sb_radius = QtWidgets.QSpinBox(self.gb_circle)
        self.sb_radius.setMaximum(999999999)
        self.sb_radius.setObjectName("sb_radius")
        self.horizontalLayout_3.addWidget(self.sb_radius)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.gb_circle)
        self.lb_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lb_result.setFont(font)
        self.lb_result.setObjectName("lb_result")
        self.verticalLayout_4.addWidget(self.lb_result)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Select shape "))
        self.cb_select_shape.setItemText(0, _translate("Form", "Square"))
        self.cb_select_shape.setItemText(1, _translate("Form", "Circle"))
        self.gb_square.setTitle(_translate("Form", "Square"))
        self.label.setText(_translate("Form", "Height"))
        self.label_2.setText(_translate("Form", "Width"))
        self.gb_circle.setTitle(_translate("Form", "Circle"))
        self.label_3.setText(_translate("Form", "Radius"))
        self.lb_result.setText(_translate("Form", "Result:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
