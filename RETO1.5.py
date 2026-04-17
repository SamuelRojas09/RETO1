def words_with_same_characters(word_list: list[str]) -> list[list[str]]:
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
