from src.drives.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import Request as FlaskRequest
from typing import Dict, List
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface)-> None:
        self.__driver_handler = driver_handler
    
    def calculate(self,request:FlaskRequest)-> Dict:
        body = request.json
        self.__validate_numbers(body)
        variance = self.__driver_handler.variance(body['numbers'])
        multiplication = self.__calculate_multiplication(body['numbers'])
        # variance < multiplica -> sucesso
        self.__verify_results(variance,multiplication)
        return self.__format_response(variance)
    
    def __validate_numbers(self, data: Dict) -> None:
        if "numbers" not in data:
            raise HttpUnprocessableEntityError("Body mal formatado!")

        elif data["numbers"] == None:
            raise HttpUnprocessableEntityError("Necessário ter  um valor")

        elif not isinstance(data["numbers"], list):
            raise HttpUnprocessableEntityError("Necessário passar uma lista de valores")

        self.__validate_type(data["numbers"])

    def __validate_type(self, data: List[float]) -> None:
        result = all(isinstance(number, (int, float)) for number in data)
        if not result:
            raise HttpUnprocessableEntityError("Valores devem ser numericos")  
    
    def __calculate_multiplication(self,numbers:List[float])->float:
        mult = 1
        for num in numbers:
            mult*=num
        return mult
    
    def __verify_results(self, variance:float,multiplication:float)->None:
        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo: Variancia menor que multiplicacao')
    
    def __format_response(self, multiplication: float) -> Dict:
        return {"data": {"Calculator": 3, 
                         "value": round(multiplication, 2),
                         "Success":True}}
    