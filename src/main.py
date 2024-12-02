import atexit
import sys

from PySide6.QtWidgets import QApplication

from model import Model
from presenter import Presenter
from view import View

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Model()
    atexit.register(m.save_history)
    widget = View()
    p = Presenter(m, widget)
    widget.set_presenter(p)
    widget.show()
    sys.exit(app.exec())
