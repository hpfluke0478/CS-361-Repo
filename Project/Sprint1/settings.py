import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class SettingScreen(QtWidgets.QMainWindow):
    def __init__(self):
        print("Initializing SettingScreen")
        super(SettingScreen, self).__init__()
        uic.loadUi('settings.ui', self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SettingScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()