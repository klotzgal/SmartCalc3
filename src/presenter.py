from model import Model
from view import IView


class Presenter():

    def __init__(self, model: Model, view: IView) -> None:
        self.model = model
        self.view = view

    def calc(self) -> None:
        self.model.expression = self.view.input
        self.model.x = float(self.view.input_x)
        self.view.input = self.model.calc()

    def plot(self) -> None:
        self.model.expression = self.view.input
        self.model.plot(limit=1000000)
        self.view.show_plot(self.model.px, self.model.py)
