from model import Graphic, Model

import sys

from PySide6.QtWidgets import QApplication
from view import View

if __name__ == '__main__':
    m = Model()
    m.expression = '2 * 2'
    print(m.calc())
    m.expression = ''
    print(m.calc())
    m.x = 32
    m.expression = 'x + 8'
    print(m.calc())
    m.plot()
    graphic: Graphic = m.plot_minmax
    print(f'{graphic=}\n{m.px=}, {m.py}')

    app = QApplication(sys.argv)
    widget = View()
    widget.show()
    sys.exit(app.exec())
