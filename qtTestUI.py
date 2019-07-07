import os
import json

from PySide2 import QtWidgets, QtCore, QtGui

from ui import ui

"""
Abstracting resources
"""
dir_path = os.path.dirname(os.path.realpath(__file__))
resource = os.path.join(dir_path, "ui", "fam_tree.json")
pic_dir = os.path.join(dir_path, "ui", "pics")


class MyQtApp(ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with open(resource) as json_file:
            data = json.loads(json_file.read())
        self.data = dict(data)
        btn_grid = 10
        for item, val in self.data.items():
            """
            Relative file path; filename from json
            """
            pic_path = os.path.join(pic_dir, "{}_{}.png".format(val["name"].split()[0], val["name"].split()[1]))

            self.pushButton = QtWidgets.QPushButton(self.frame)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(pic_path))
            self.pushButton.setIcon(icon)
            self.pushButton.setGeometry(QtCore.QRect(10, btn_grid, 251, 71))
            self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", val["name"], None, -1))
            self.pushButton.clicked.connect(self.clicked)
            btn_grid += 70
            self.pushButton.picture = pic_path
            self.pushButton.description = val["desc"]

    def clicked(self):
        """
        Change label based on what button was pressed
        """
        button = self.sender()
        if isinstance(button, type(self.pushButton)):
            """
            Adapt picture size to label frame
            """
            pixmap = QtGui.QPixmap(button.picture)
            pixmap_resized = pixmap.scaled(240, 210, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap_resized)
            self.label_2.setText("%s" % button.text())
            self.label_3.setText("%s" % button.description)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()