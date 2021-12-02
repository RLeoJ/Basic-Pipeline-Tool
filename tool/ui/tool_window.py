import six

from Qt import QtCompat, QtWidgets, QtCore

import os

from tool.ui import data

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

from handler.choose_handler import choose_handler as handler

ui_path = Path(__file__).parent / 'qt' / 'Window.ui'

UserRole = QtCore.Qt.UserRole

class ToolWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)
        self.handler = handler()

        for f in data.get_files():
            addListWidgetItem(self.listWidget, f, os.path.basename(f))

        self.create_buttons()

    def create_buttons(self):
        for implementation in self.handler.implements:
            button = QtWidgets.QPushButton(implementation)
            button.setToolTip(implementation)
            button.setText(implementation)
            self.verticalLayout.addWidget(button)
            button.clicked.connect(self.assign_function)

    def assign_function(self):
        button_name = self.sender().text()
        if 'Open' in button_name:
            self.open_file()
        elif 'Save' in button_name:
            self.save_file()
        else:
            self.custom_function()

    def open_file(self):
        item = self.listWidget.currentItem()
        path = item.data(UserRole)
        self.handler.open(path)

    def save_file(self):
        self.handler.save()

    def custom_function(self):
        item = self.listWidget.currentItem()
        path = item.data(UserRole)
        self.handler.reference(path)

def addListWidgetItem(listWidget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    listWidget.addItem(item)
    return item

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()
