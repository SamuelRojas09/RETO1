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
