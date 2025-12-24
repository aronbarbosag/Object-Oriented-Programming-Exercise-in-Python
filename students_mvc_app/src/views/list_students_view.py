class ListStudentView:
    def list(self, student_list: list) -> str:
        message = f"""
        Count: {len(student_list)}
        Data: {str(student_list)}

        """

        print(message)
