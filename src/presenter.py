from model import Model
from view import IView


class Presenter():

    def __init__(self, model: Model, view: IView) -> None:
        self.model = model
        self.view = view

    def calc(self) -> None:
        self.view.set_input(self.model.calc())
