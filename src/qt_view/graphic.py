from PySide6.QtWidgets import QWidget, QVBoxLayout

from qt_view.ui_graphic import Ui_Graphic
import pyqtgraph as pg
import numpy as np


class Graphic(QWidget):

    def __init__(self, parent=None, main_window=None) -> None:
        super().__init__(parent)
        self.main_window = main_window
        self.ui = Ui_Graphic()
        self.ui.setupUi(self)
        layout = QVBoxLayout(self.ui.plot)
        self.ui.plot.setLayout(layout)
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        self.ui.button_back.clicked.connect(
            self._button_back_slot
        )

    def _button_back_slot(self) -> None:
        self.main_window.show()
        self.close()

    def print_plot(self, x: np.ndarray, y: np.ndarray) -> None:
        self.plot_widget.clear()
        self.plot_widget.plot(x, y, pen=pg.mkPen(color="r", width=2))
