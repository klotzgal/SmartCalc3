import ctypes
import pathlib


class Graphic(ctypes.Structure):
    _fields_ = [('xMin', ctypes.c_double),
                ('xMax', ctypes.c_double),
                ('yMin', ctypes.c_double),
                ('yMax', ctypes.c_double),]


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

    return lib


lib = import_cpp()


class Model:
    def __init__(self) -> None:
        self.model = lib.model_new()
        self._expression: str = ''
        self._x: float = 0
        self._plot: Graphic = Graphic

    def __del__(self):
        lib.model_del(self.model)

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

    def calc(self) -> str:
        try:
            print("|", self._expression, "|= ", end='')
            lib.set_x(self.model, self._x)
            lib.set_string(self.model, self._expression.encode())
            res: str = lib.calc(self.model).decode('utf-8')
        except Exception as err:
            res: str = str(err)
        return res
