import ctypes
import pathlib


class Graphic(ctypes.Structure):
    _fields_ = [
        ('xMin', ctypes.c_double),
        ('xMax', ctypes.c_double),
        ('yMin', ctypes.c_double),
        ('yMax', ctypes.c_double),
    ]

    def __repr__(self) -> str:
        return f'xMin={self.xMin}, xMax={self.xMax}, yMin={self.yMin}, yMax={self.yMax}'


def import_cpp() -> ctypes.CDLL:
    libname: str = pathlib.Path().absolute() / './build/obj/model.so'
    lib: ctypes.CDLL = ctypes.CDLL(libname)

    lib.model_new.restype = ctypes.c_void_p
    lib.set_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.calc.restype = ctypes.c_char_p
    lib.calc.argtypes = [ctypes.c_void_p]
    lib.model_del.argtypes = [ctypes.c_void_p]
    lib.set_x.argtypes = [ctypes.c_void_p, ctypes.c_double]
    lib.plot.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_double]
    lib.get_plot.argtypes = [ctypes.c_void_p]
    lib.get_plot.restype = Graphic
    lib.get_pxi.restype = ctypes.c_double
    lib.get_pxi.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib.len_px.restype = ctypes.c_int
    lib.len_px.argtypes = [ctypes.c_void_p]
    lib.get_pyi.restype = ctypes.c_double
    lib.get_pyi.argtypes = [ctypes.c_void_p, ctypes.c_int]
    lib.len_py.restype = ctypes.c_int
    lib.len_py.argtypes = [ctypes.c_void_p]
    lib.credit_model_new.restype = ctypes.c_void_p
    lib.credit_model_del.argtypes = [ctypes.c_void_p]
    lib.credit_calc.restype = ctypes.c_char_p
    lib.credit_calc.argtypes = [
        ctypes.c_void_p,
        ctypes.c_double,
        ctypes.c_double,
        ctypes.c_double,
        ctypes.c_bool,
    ]
    lib.get_first_payment.restype = ctypes.c_double
    lib.get_first_payment.argtypes = [ctypes.c_void_p]
    lib.get_last_payment.restype = ctypes.c_double
    lib.get_last_payment.argtypes = [ctypes.c_void_p]
    lib.get_overpayment.restype = ctypes.c_double
    lib.get_overpayment.argtypes = [ctypes.c_void_p]
    lib.get_total.restype = ctypes.c_double
    lib.get_total.argtypes = [ctypes.c_void_p]
    return lib


lib: ctypes.CDLL = import_cpp()


class Model:
    def __init__(self) -> None:
        self._model = lib.model_new()
        self._credit_model = lib.credit_model_new()
        self._expression: str = ''
        self._x: float = 0
        self._plot: Graphic = Graphic
        self._px: list[float] = []
        self._py: list[float] = []
        self._every_month_payment: str = ''
        self._overpayment: float = 0
        self._total: float = 0
        self._history: list[str] = []
        try:
            with open('.history', 'r') as f:
                for line in f:
                    self._history.append(line.strip())
        except FileNotFoundError:
            pass
        self._history_index: int = len(self._history)

    def __del__(self) -> None:
        lib.model_del(self._model)
        lib.credit_model_del(self._credit_model)

    def calc(self) -> str:
        lib.set_x(self._model, self._x)
        lib.set_string(self._model, self._expression.encode())
        self._history.append(self._expression)
        self._history_index = len(self._history)
        res: str = lib.calc(self._model).decode('utf-8')
        return res

    def credit_calc(self, S: float, n: float, p: float, annuity: bool = True) -> None:
        lib.credit_calc(self._credit_model, S, n, p, annuity)
        self._overpayment = round(lib.get_overpayment(self._credit_model), 2)
        self._every_month_payment = str(
            round(lib.get_first_payment(self._credit_model), 2)
        )
        last = lib.get_last_payment(self._credit_model)
        if last != -1:
            self._every_month_payment += '\n' + str(round(last, 2))
        self._total = round(lib.get_total(self._credit_model), 2)

    def plot(self, autoscale: bool = False, limit: float = 10) -> None:
        lib.set_string(self._model, self._expression.encode())
        lib.plot(self._model, autoscale, limit)
        self._update_plot_info()

    def _update_plot_info(self) -> None:
        length = min(lib.len_px(self._model), lib.len_py(self._model))
        self._px, self._py = [], []
        self._plot = lib.get_plot(self._model)
        for i in range(length):
            self._px.append(lib.get_pxi(self._model, i))
            self._py.append(lib.get_pyi(self._model, i))

    @property
    def expression(self) -> str:
        return self._expression

    @expression.setter
    def expression(self, value: str) -> None:
        self._expression = value

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @property
    def plot_minmax(self) -> Graphic:
        return self._plot

    @property
    def px(self) -> list[float]:
        if self._px == []:
            self._update_plot_info()
        return self._px

    @property
    def py(self) -> list[float]:
        if self._py == []:
            self._update_plot_info()
        return self._py

    @property
    def every_month_payment(self) -> str:
        return self._every_month_payment

    @property
    def overpayment(self) -> float:
        return self._overpayment

    @property
    def total(self) -> float:
        return self._total

    @property
    def history_prev(self) -> str:
        if self._history_index > 0:
            self._history_index -= 1
            return self._history[self._history_index]

    @property
    def history_next(self) -> str:
        if self._history_index < len(self._history) - 1:
            self._history_index += 1
            return self._history[self._history_index]

    def history_clear(self) -> None:
        self._history = []
        self._history_index = 0

    def save_history(self) -> None:
        with open('.history', 'w') as f:
            for line in self._history:
                f.write(line + '\n')
