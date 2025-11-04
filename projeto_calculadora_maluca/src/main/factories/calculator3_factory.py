from src.drives.numpy_handle import NumpyHandle
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
    numpy_handler = NumpyHandle()
    calc = Calculator3(numpy_handler)
    return calc