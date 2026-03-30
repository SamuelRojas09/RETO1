"""
El programa recorre todas las palabras que el usuario ingresó y busca cuáles tienen los mismos caracteres.
Primero pido las palabras con input() y uso split() para separar la cadena en palabras individuales.
Luego tomo cada palabra como base y comparo sus letras con las de todas las demás palabras que todavía no hayan sido agrupadas.
Para comparar, uso sorted() que ordena las letras de cada palabra 
y así puedo verificar si tienen exactamente los mismos caracteres, letra por letra.
Para no repetir palabras en varios grupos, uso una lista que marca cuáles palabras ya fueron incluidas en algún grupo. 
Si todas las letras coinciden con la palabra base, agrego esa palabra al grupo y la marco como usada.
Al final, guardo solo los grupos que tienen más de una palabra, porque esos son los que realmente comparten los mismos caracteres. 
Finalmente, muestro cada grupo en pantalla, indicando cuáles palabras tienen exactamente los mismos caracteres entre sí.
"""

def words_with_same_characters(word_list: list[str]):
    result: list[list[str]] = []
    used: list[bool] = [False] * len(word_list)
    index: int = 0

    while index < len(word_list):
        if used[index]:
            index += 1
            continue

        base_word: str = word_list[index]
        base_letters: list[str] = sorted(base_word)
        group: list[str] = [base_word]
        used[index] = True

        other_index: int = index + 1
        while other_index < len(word_list):
            if not used[other_index]:
                current_word: str = word_list[other_index]
                current_letters: list[str] = sorted(current_word)
                are_equal: bool = True

                if len(base_letters) != len(current_letters):
                    are_equal = False
                else:
                    position: int = 0
                    while position < len(base_letters):
                        if base_letters[position] != current_letters[position]:
                            are_equal = False
                            break
                        position += 1

                if are_equal:
                    group.append(current_word)
                    used[other_index] = True

            other_index += 1

        if len(group) > 1:
            result.append(group)

        index += 1

    return result


while True:
    user_input: str = input("Ingrese palabras separadas por espacios: ")
    words: list[str] = []
    parts: list[str] = user_input.split()
    position: int = 0

    while position < len(parts):
        word: str = parts[position]
        words.append(word)
        position += 1

    if len(words) == 0:
        print("Debe ingresar al menos una palabra.")
        continue

    break


result: list[list[str]] = words_with_same_characters(words)

if len(result) == 0:
    print("No se encontraron palabras con los mismos caracteres.")
else:
    for group in result:
        print("Palabras con los mismos caracteres:", group)
