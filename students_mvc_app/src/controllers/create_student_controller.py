class CreateStudentController:
    def create(self, view_response: dict):
        try:
            self.__validate(view_response)

            response = self.__format_response(view_response)

            return {"success": True, "message": response}

        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate(self, view_response: dict) -> None:
        try:
            _id = int(view_response["matricula"])
        except Exception as exception:
            raise Exception("Tipo do campo id deve conter apenas numeros!")

        try:
            name = str(view_response["nome"])
        except Exception as exception:
            raise Exception("Tipo do campo name deve conter apenas letras!")

        try:
            cr = float(view_response["CR"])
        except Exception as exception:
            raise Exception("Tipo do campo cr deve conter apenas numeros!")

    def __format_response(self, view_response: dict) -> dict:
        response = {
            "Count": 1,
            "Attributes": {
                "id": int(view_response["matricula"]),
                "name": view_response["nome"],
                "cr": float(view_response["CR"]),
            },
        }

        return response
