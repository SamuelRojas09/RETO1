"""
Definí la función operaciones que recibe dos números y un operador. 
Según el operador, realiza suma, resta, multiplicación o división (verificando que no sea división entre cero). 
Si el operador es inválido, devuelve un mensaje de error. 
Luego, con input(), pido los números y el operador al usuario,
y uso try-except para manejar errores si ingresa algo que no sea un número.
"""

def operations(number_1: int, number_2: int, character: str) -> float | str:

    if character == "+":
        return number_1 + number_2

    elif character == "-":
        return number_1 - number_2

    elif character == "*":
        return number_1 * number_2

    elif character == "/":
        if number_2 != 0:
            return number_1 / number_2
        return "Error: no se puede dividir entre cero"

    return "Ingreso un caracter invalido"


number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
character = input("Ingrese el signo de la operación (+, -, *, /): ")

print(operations(number_1, number_2, character))
