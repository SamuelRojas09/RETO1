def is_palindrome(word: str) -> bool:
    word = word.lower()
    length: int = len(word)
    start_index: int = 0
    end_index: int = length - 1
    is_palindrome_word: bool = True

    while start_index < end_index:
        start_letter: str = word[start_index]
        end_letter: str = word[end_index]

        if start_letter != end_letter:
            is_palindrome_word = False
            break

        start_index += 1
        end_index -= 1

    return is_palindrome_word


user_word: str = input("Ingrese una palabra: ")
result: bool = is_palindrome(user_word)

if result:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")
