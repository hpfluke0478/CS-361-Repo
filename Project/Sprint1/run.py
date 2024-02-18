import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class RunScreen(QtWidgets.QMainWindow):
    def __init__(self):
        print("Initializing RunScreen")
        super(RunScreen, self).__init__()
        uic.loadUi('run.ui', self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RunScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()