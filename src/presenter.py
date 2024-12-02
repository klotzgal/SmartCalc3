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

    def credit_calc(self, S: float, n: float, p: float, annuity: bool = True) -> None:
        self.model.credit_calc(S, n, p, annuity)
        self.view.show_credit(
            self.model.every_month_payment,
            self.model.total,
            self.model.overpayment,
        )

    def history_prev(self) -> None:
        value = self.model.history_prev
        if value:
            self.view.input = value

    def history_next(self) -> None:
        value = self.model.history_next
        if value:
            self.view.input = value

    def history_clear(self) -> None:
        self.model.history_clear()
