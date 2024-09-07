import ctypes
import pathlib


def import_cpp() -> ctypes.CDLL:
    libname = pathlib.Path().absolute() / './lib/obj/model.so'
    lib = ctypes.CDLL(libname)

    lib.model_new.restype = ctypes.c_void_p
    lib.set_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    lib.calc.restype = ctypes.c_double
    lib.model_del.argtypes = [ctypes.c_void_p]
    return lib


lib = import_cpp()


class Model:
    def __init__(self) -> None:
        self.model = lib.model_new()
        self._expression = ''

    @property
    def expression(self) -> str:
        return self._expression

    @expression.setter
    def expression(self, value: str) -> None:
        self._expression = value

    def calc(self) -> str:
        try:
            print(self._expression.encode())
            res = str(lib.calc(self.model, self._expression.encode()))
        except Exception as err:
            res = str(err)
        return res
    
    def __del__(self):
        lib.model_del(self.model)
