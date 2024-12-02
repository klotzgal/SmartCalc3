# This Python file uses the following encoding: utf-8
from typing import Any

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from qt_view.credit import CreditWindow
from qt_view.graphic import GraphicWindow
from qt_view.ui_form import Ui_View


class IView:
    @property
    def input(self) -> str: ...

    @input.setter
    def input(self, text: str) -> None: ...

    @property
    def input_x(self) -> str: ...

    @input_x.setter
    def input_x(self, text: str) -> None: ...

    def set_presenter(self, presenter: Any) -> None: ...

    def show_plot(
        self,
        x: list[float],
        y: list[float],
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
    ) -> None: ...

    def show_credit(
        self, every_month_payment: str, total: float, overpayment: float
    ) -> None: ...


class View(IView, QMainWindow):
    def __init__(self, parent=None, presenter=None) -> None:
        super().__init__(parent)
        self.presenter: Any = presenter
        self.ui = Ui_View()
        self.ui.setupUi(self)
        self.setWindowTitle('S21 Calculator')
        self.graphic_window = GraphicWindow(main_window=self)
        self.credit_window = CreditWindow(main_window=self)
        self._limit: int = 10

        self.ui.button_plot.clicked.connect(self._button_plot_slot)
        self.ui.button_credit.clicked.connect(self._button_credit_slot)

        self.ui.button_equal.setCheckable(True)
        self.ui.button_equal.setChecked(True)
        self.ui.button_equal.clicked.connect(self._button_equal_slot)
        self.ui.button_c.clicked.connect(self._button_clear_slot)
        self.ui.button_ac.clicked.connect(self._button_all_clear_slot)

        for button in self.ui.input_buttons.buttons():
            button.clicked.connect(self._print_in_input_slot)

        self.ui.input.setValidator(
            QRegularExpressionValidator(QRegularExpression(r'^[^\s]+$'))
        )

    def set_presenter(self, presenter: Any) -> None:
        self.presenter = presenter
        self.ui.history_prev.clicked.connect(self.presenter.history_prev)
        self.ui.history_next.clicked.connect(self.presenter.history_next)
        self.ui.history_clear.clicked.connect(self.presenter.history_clear)

    def show_plot(
        self,
        x: list[float],
        y: list[float],
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
    ) -> None:
        self.graphic_window.print_plot(x, y, x_min, x_max, y_min, y_max)

    def show_credit(
        self, every_month_payment: str, total: float, overpayment: float
    ) -> None:
        self.credit_window.print_credit(every_month_payment, total, overpayment)

    def _print_in_input_slot(self) -> None:
        if self.ui.button_equal.isChecked():
            self.ui.input.setText('')
            self.ui.button_equal.setChecked(False)

        button: QPushButton = self.sender()
        txt: str = button.text()
        if txt == '%':
            txt = ' mod '
        if txt in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'sqrt']:
            txt += '('
        self.ui.input.setText(self.ui.input.text() + txt)

    def _button_equal_slot(self) -> None:
        if self.presenter is not None:
            self.presenter.calc()
        self.ui.button_equal.setChecked(True)

    def _button_clear_slot(self) -> None:
        self.ui.input.setText(self.ui.input.text()[:-1])

    def _button_all_clear_slot(self) -> None:
        self.ui.input.setText('0')
        self.ui.button_equal.setChecked(True)

    def _button_plot_slot(self) -> None:
        self.graphic_window.plot.expression = 'y=' + str(self.ui.input.text())
        self.presenter.plot(self.graphic_window.ui.autoscale.isChecked(), self._limit)
        self.graphic_window.show()
        self.close()

    def _button_credit_slot(self) -> None:
        self.credit_window.show()
        self.close()

    @property
    def input(self) -> str:
        return self.ui.input.text()

    @input.setter
    def input(self, text: str) -> None:
        self.ui.input.setText(text)

    @property
    def input_x(self) -> str:
        return self.ui.input_x.text()

    @input_x.setter
    def input_x(self, text: str) -> None:
        self.ui.input_x.setText(text)
