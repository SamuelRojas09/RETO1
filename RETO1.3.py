"""
Primero definí la función es_primo, que recibe un número y verifica si es primo. 
Si el número es menor o igual a 1, devuelve False. 
Luego, con un bucle while, revisa si existe algún divisor desde 2 hasta la raíz cuadrada del número; si encuentra uno, devuelve False, y si no, devuelve True.
Después definí la función obtener_primos, que recibe una lista de números y recorre cada número. 
Si el número es primo (usando la función anterior), lo agrega a una nueva lista de primos.
Finalmente, pido al usuario que ingrese números separados por comas y los convierto a enteros. 
Llamo a obtener_primos con esa lista y muestro tanto la lista original como los números primos.
También agregué un try-except para manejar errores si el usuario ingresa algo que no sean números enteros.
"""

def is_prime(number: int):
    
    if number <= 1:
        return False

    divisor: int = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_primes(number_list: list[int]):

    prime_list: list[int] = []

    for number in number_list:
        if is_prime(number):
            prime_list.append(number)

    return prime_list


try:
    user_input: str = input("Ingrese números separados por coma (ej: 4,7,9,11,15): ")

    number_list: list[int] = [
        int(number.strip()) for number in user_input.split(",")
    ]

    result = get_primes(number_list)

    print("Lista original:", number_list)
    print("Números primos:", result)

except ValueError:
    print("Error: debe ingresar solo números enteros separados por comas.")
