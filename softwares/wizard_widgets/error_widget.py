# coding: utf-8
# Author: Mael PERON
# Contact: maelperon.cg@gmail.com

# Python modules
import os
import sys
try:
    from PyQt6 import QtWidgets, QtCore, QtGui
except ModuleNotFoundError:
    try:
        from PySide6 import QtWidgets, QtCore, QtGui
    except Exception as e:
        if isinstance(e, ModuleNotFoundError) or isinstance(e, ImportError):
            from PySide2 import QtWidgets, QtCore, QtGui


import logging

# Wizard modules
import wizard_communicate

logger = logging.getLogger(__name__)

dialog_accepted = QtWidgets.QDialog.DialogCode.Accepted

if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)



class error_widget(QtWidgets.QDialog):
    def __init__(self, error_message, parent=None):
        super(error_widget, self).__init__(parent)

        self.setWindowTitle("Wizard - Error")
        self.setMinimumWidth(400)

        self.error_message = error_message

        self.build_ui()
        self.fill_ui()
        self.connect_functions()

    def build_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.error_label = QtWidgets.QLabel(self)
        self.error_label.setWordWrap(True)
        self.error_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred
        )
        self.main_layout.addWidget(self.error_label)

        self.ok_button = QtWidgets.QPushButton("OK", self)
        self.main_layout.addWidget(self.ok_button)

    def fill_ui(self):
        self.error_label.setText(self.error_message)

    def connect_functions(self):
        self.ok_button.clicked.connect(self.accept)
