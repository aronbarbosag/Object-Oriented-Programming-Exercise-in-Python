from src.calculators.calculator_2 import Calculator2
from src.drives.numpy_handle import NumpyHandle

def calculator2_factory():
    numpy_handler = NumpyHandle()
    calc = Calculator2(numpy_handler)
    return calc