import sys

from PySide6.QtWidgets import QApplication

from model import Model
from presenter import Presenter
from view import View

if __name__ == '__main__':
    m = Model()
    # m.expression = '2 * 2'
    # print(m.calc())
    # m.expression = ''
    # print(m.calc())
    # m.x = 32
    # m.expression = 'x + 8'
    # print(m.calc())
    # m.plot()
    # graphic: Graphic = m.plot_minmax
    # print(f'{graphic=}\n{m.px=}, {m.py}')

    m.credit_calc(60000, 12, 12, False)
    print(f'{m.every_month_payment=}, {m.overpayment=}, {m.total=}')

    app = QApplication(sys.argv)

    widget = View()
    p = Presenter(m, widget)
    widget.set_presenter(p)
    widget.show()
    sys.exit(app.exec())
