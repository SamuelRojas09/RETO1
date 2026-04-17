def is_prime(number: int) -> bool:
    
    if number <= 1:
        return False

    divisor: int = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_primes(number_list: list[int]) -> list[int]:

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
