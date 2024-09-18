# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from qt_view.ui_form import Ui_View


class IView:

    @property
    def input(self) -> str:
        ...

    @input.setter
    def input(self, text: str) -> None:
        ...


class View(IView, QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_View()
        self.ui.setupUi(self)

        self.ui.button_equal.setCheckable(True)
        self.ui.button_equal.clicked.connect(
            self._button_equal_slot
        )
        self.ui.button_c.clicked.connect(
            self._button_clear_slot
        )
        self.ui.button_ac.clicked.connect(
            self._button_all_clear_slot
        )

        for btn in self.ui.input_buttons.buttons():
            btn.clicked.connect(
                self._print_in_input_slot
            )

        self.ui.input.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(r'^[^\s]+$')
            )
        )

    def _print_in_input_slot(self) -> None:
        if self.ui.button_equal.isChecked():
            self.ui.input.setText('')
            self.ui.button_equal.setChecked(False)

        btn: QPushButton = self.sender()
        txt: str = btn.text()
        if txt == '%':
            txt = ' mod '
        if txt in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'sqrt']:
            txt += '('
        self.ui.input.setText(self.ui.input.text() + txt)

    def _button_equal_slot(self) -> None:
        # TODO: Вызов презентера с self.ui.input.text() и self.ui.input_x.text()
        self.ui.button_equal.setChecked(True)

    def _button_clear_slot(self) -> None:
        self.ui.input.setText(self.ui.input.text()[:-1])

    def _button_all_clear_slot(self) -> None:
        self.ui.input.setText('0')
        self.ui.button_equal.setChecked(True)

    @property
    def input(self) -> str:
        return self.ui.input.text()

    @input.setter
    def input(self, text: str) -> None:
        self.ui.input.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = View()
    widget.show()
    sys.exit(app.exec())
