from qtpy.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


main()
