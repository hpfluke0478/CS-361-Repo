import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class TitleScreen(QtWidgets.QMainWindow):
    def __init__(self):
        print("Initializing TitleScreen")
        super(TitleScreen, self).__init__()
        uic.loadUi('title.ui', self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TitleScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()