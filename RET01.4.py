"""
El programa calcula la mayor suma entre dos números consecutivos dentro de una lista.
Primero, se define la función max_consecutive_sum, la cual recibe una lista de enteros
y verifica que tenga al menos dos elementos.
Luego, recorre la lista utilizando un ciclo while, calcula la suma de cada par consecutivo 
y guarda la mayor suma encontrada.
El programa solicita al usuario una serie de números separados por espacios. 
Estos valores se convierten a enteros y se almacenan en una lista mediante un bloque try-except,
que permite manejar errores si la entrada no es válida.
Finalmente, la lista obtenida se pasa a la función, 
y se muestra el resultado correspondiente a la mayor suma consecutiva.
"""

def max_consecutive_sum(number_list: list[int]) -> int:
    if len(number_list) < 2:
        return 0

    current_sum: int = number_list[0] + number_list[1]
    max_sum: int = current_sum

    index: int = 1

    while index < len(number_list) - 1:
        current_number: int = number_list[index]
        next_number: int = number_list[index + 1]

        current_sum = current_number + next_number

        if current_sum > max_sum:
            max_sum = current_sum

        index += 1

    return max_sum


while True:
    user_input: str = input("Ingrese los números separados por espacios: ")
    numbers: list[int] = []

    try:
        for num in user_input.split():
            numbers.append(int(num))  

        if len(numbers) < 2:
            print("Debe ingresar al menos dos números.")
            continue

        break 

    except ValueError:
        print("Entrada inválida. Solo ingrese números enteros separados por espacios.")

result: int = max_consecutive_sum(numbers)
print("La mayor suma consecutiva es:", result)
