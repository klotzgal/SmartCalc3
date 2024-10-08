from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QWidget

from qt_view.ui_credit import Ui_Credit


class CreditWindow(QWidget):
    def __init__(self, parent=None, main_window=None) -> None:
        super().__init__(parent)
        self.main_window = main_window
        self.ui = Ui_Credit()
        self.ui.setupUi(self)
        self.setWindowTitle('Credit Calculator')

        self.ui.button_back.clicked.connect(self._button_back_slot)
        self.ui.button_calc.clicked.connect(self._button_calc_slot)
        self.ui.line_edit_mounth.setValidator(
            QDoubleValidator(0.0, 1000000.0, 10, self.ui.line_edit_mounth)
        )
        self.ui.line_edit_percent.setValidator(
            QDoubleValidator(0.0, 100.0, 10, self.ui.line_edit_percent)
        )
        self.ui.line_edit_summ.setValidator(
            QDoubleValidator(0.0, 1000000.0, 10, self.ui.line_edit_summ)
        )

    def print_credit(
        self, every_month_payment: str, total: float, overpayment: float
    ) -> None:
        self.ui.every_month_payment.setText(every_month_payment)
        self.ui.total.setText(str(total))
        self.ui.overpayment.setText(str(overpayment))

    def _button_back_slot(self) -> None:
        self.main_window.show()
        self.close()

    def _button_calc_slot(self) -> None:
        if self.main_window.presenter is not None:
            self.main_window.presenter.credit_calc(
                float(self.ui.line_edit_summ.text() or 0),
                float(self.ui.line_edit_mounth.text() or 0),
                float(self.ui.line_edit_percent.text() or 0),
                self.ui.annuity.isChecked(),
            )
