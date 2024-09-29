from model import Model
from view import IView


class Presenter:
    def __init__(self, model: Model, view: IView) -> None:
        self.model = model
        self.view = view

    def calc(self) -> None:
        self.model.expression = self.view.input
        self.model.x = float(self.view.input_x)
        self.view.input = self.model.calc()

    def plot(self, autoscale: bool = False, limit: float = 10) -> None:
        self.model.expression = self.view.input
        self.model.plot(autoscale, limit=limit)
        minmax = self.model.plot_minmax
        self.view.show_plot(
            self.model.px,
            self.model.py,
            minmax.xMin,
            minmax.xMax,
            minmax.yMin,
            minmax.yMax,
        )
