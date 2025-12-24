from src.main.constructor.create_student_constructor import create_student_constructor
from src.main.constructor.edit_student_constructor import edit_student_constructor
from src.main.constructor.list_students_constructor import list_students_constructor
from src.views.menu_view import show_menu


def start():
    while True:
        show_menu()
        command = int(input(""))

        if command == 0:
            break
        elif command == 1:
            print(f"Comando {command}\n\n")
            create_student_constructor()

        elif command == 2:
            print(f"Comando {command}\n\n")
            list_students_constructor()

        elif command == 3:
            print(f"Comando {command}\n\n")
            edit_student_constructor()
        elif command == 4:
            print(f"Comando {command}\n\n")
        else:
            print("Comando não encontrado!")
