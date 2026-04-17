## RETO 1-1
Definí la función operaciones que recibe dos números y un operador. 
Según el operador, realiza suma, resta, multiplicación o división (verificando que no sea división entre cero). 
Si el operador es inválido, devuelve un mensaje de error. 
Luego, con input(), pido los números y el operador al usuario,
y uso try-except para manejar errores si ingresa algo que no sea un número.

## RETO 1-2
Definí la función es_palindromo, que recibe una palabra y la convierte a minúsculas 
para que la comparación no dependa de mayúsculas o minúsculas. 
Luego utilizo dos índices, uno al inicio y otro al final de la palabra, 
y voy comparando letra por letra mientras los índices avanzan hacia el centro.
Si encuentro alguna diferencia, la función marca que la palabra no es un palíndromo y termina la verificación. 
Después, pido la palabra al usuario con input(), llamo a la función 
y muestro un mensaje indicando si la palabra ingresada es o no un palíndromo.

## RETO 1-3
Primero definí la función es_primo, que recibe un número y verifica si es primo. 
Si el número es menor o igual a 1, devuelve False. 
Luego, con un bucle while, revisa si existe algún divisor desde 2 hasta la raíz cuadrada del número; 
si encuentra uno, devuelve False, y si no, devuelve True.
Después definí la función obtener_primos, que recibe una lista de números y recorre cada número. 
Si el número es primo (usando la función anterior), lo agrega a una nueva lista de primos.
Finalmente, pido al usuario que ingrese números separados por comas y los convierto a enteros. 
Llamo a obtener_primos con esa lista y muestro tanto la lista original como los números primos.
También agregué un try-except para manejar errores si el usuario ingresa algo que no sean números enteros.

## RETO 1-4
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
