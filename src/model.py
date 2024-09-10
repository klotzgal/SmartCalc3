import ctypes
import pathlib


class Graphic(ctypes.Structure):
    _fields_ = [('xMin', ctypes.c_double),
                ('xMax', ctypes.c_double),
                ('yMin', ctypes.c_double),
                ('yMax', ctypes.c_double),]

    def __repr__(self) -> str:
        return f'xMin={self.xMin}, xMax={self.xMax}, yMin={self.yMin}, yMax={self.yMax}'


def import_cpp() -> ctypes.CDLL:
    libname = pathlib.Path().absolute() / './lib/obj/model.so'
    lib = ctypes.CDLL(libname)

    lib.model_new.restype = ctypes.c_void_p
    lib.set_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.calc.restype = ctypes.c_char_p
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

    return lib


lib = import_cpp()


class Model:
    def __init__(self) -> None:
        self._model = lib.model_new()
        self._expression: str = ''
        self._x: float = 0
        self._plot: Graphic = Graphic
        self._px: list[float] = []
        self._py: list[float] = []

    def __del__(self):
        lib.model_del(self._model)

    def calc(self) -> str:
        print("|", self._expression, "|= ", end='')
        lib.set_x(self._model, self._x)
        lib.set_string(self._model, self._expression.encode())
        res: str = lib.calc(self._model).decode('utf-8')
        return res

    def plot(self, autoscale: bool = False, limit: float = 10):
        lib.plot(self._model, autoscale, limit)
        self._update_plot_info()

    def _update_plot_info(self):
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
    def plot_minmax(self):
        return self._plot

    @property
    def px(self):
        if self._px == []:
            self._update_plot_info()
        return self._px

    @property
    def py(self):
        if self._py == []:
            self._update_plot_info()
        return self._py
