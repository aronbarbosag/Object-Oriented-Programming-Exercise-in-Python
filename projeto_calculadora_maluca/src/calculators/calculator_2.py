# Segunda Calculadora
# N numeros são enviados
# Todos esses N numeros sao multiplicados por 11 e elebdos a potencia de 0.95
# Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result)
from flask import Request as FlaskRequest
from typing import List, Dict
from src.drives.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator2:
    
    def __init__(self, driver_handler: DriverHandlerInterface)-> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        data = request.json
        self.__validate_numbers(data)
        first_part = self.__mult_exp(data)
        second_part = self.__inverse_std(first_part)

        return self.__format_response(second_part)

    def __mult_exp(self, data: List[float]) -> List[float]:
        numbers = data["numbers"]
        result = [(number * 11) ** 0.95 for number in numbers]
        return result

    def __inverse_std(self, numbers: List[float]) -> float:
        return 1 / self.__driver_handler.standard_deviation(numbers)

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

    def __format_response(self, result: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(result, 2)}}
