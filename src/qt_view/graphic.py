from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout, QWidget

from qt_view.ui_graphic import Ui_Graphic


class GraphicWindow(QWidget):
    def __init__(self, parent=None, main_window=None) -> None:
        super().__init__(parent)
        self.main_window = main_window
        self.ui = Ui_Graphic()
        self.ui.setupUi(self)
        self.setWindowTitle('Plot')
        layout = QVBoxLayout(self.ui.plot)
        self.ui.plot.setLayout(layout)
        self.plot = PlotCanvas(self)
        layout.addWidget(self.plot)

        self.ui.button_back.clicked.connect(self._button_back_slot)

        self.ui.slider.sliderReleased.connect(self._slider_slot)

        self.ui.limit.textChanged.connect(self._limit_slot)
        self.ui.autoscale.stateChanged.connect(self.main_window._button_plot_slot)

    def _button_back_slot(self) -> None:
        self.main_window.show()
        self.close()

    def print_plot(
        self,
        x: list[float],
        y: list[float],
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
    ) -> None:
        self.plot.plot(x, y, x_min, x_max, y_min, y_max)

    def _slider_slot(self) -> None:
        self.main_window._limit = self.ui.slider.value()
        self.main_window._button_plot_slot()

    def _limit_slot(self) -> None:
        self.main_window._limit = float(self.ui.limit.text())
        self.main_window._button_plot_slot()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)
        self.setParent(parent)
        self.expression = ''

        # Стили
        self.bg_color = '#1c1c1e'
        self.text_color = '#e5e5e5'
        self.figure.set_facecolor(self.bg_color)
        self.axes.set_facecolor(self.bg_color)

        self.axes.title.set_fontsize(14)
        self.axes.title.set_fontweight('bold')
        self.axes.title.set_color(self.text_color)
        self.axes.xaxis.label.set_color(self.text_color)
        self.axes.yaxis.label.set_color(self.text_color)

        self.axes.tick_params(axis='x', colors=self.text_color)
        self.axes.tick_params(axis='y', colors=self.text_color)
        self.axes.spines['bottom'].set_color(self.text_color)
        self.axes.spines['left'].set_color(self.text_color)

    def plot(self, x_data, y_data, x_min, x_max, y_min, y_max) -> None:
        self.axes.clear()
        self.axes.set_xlim(x_min, x_max)
        self.axes.set_ylim(y_min, y_max)
        self.axes.scatter(x_data, y_data, s=1, color='#567890')
        self.axes.set_title(
            self.expression, color=self.text_color, fontname='Open Sans'
        )
        self.draw()
