import numpy as np
from typing import List
from.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandle(DriverHandlerInterface):
    def __init__(self)-> None:
        self.__np =np
        
    def standard_deviation(self,numbers:List[float])-> float:
        return self.__np.std(numbers)
    
    def standard_deviation_with_param(self,numbers:List[float],**kwargs)-> float:
        return self.__np.std(numbers,kwargs)
    
    def variance(self,numbers:List[float])-> float:
        return self.__np.var(numbers)