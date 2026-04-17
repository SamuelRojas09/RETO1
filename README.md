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

## RETO 1-5

El programa recorre todas las palabras que el usuario ingresó y busca cuáles tienen los mismos caracteres.
Primero pido las palabras con input() y uso split() para separar la cadena en palabras individuales.
Luego tomo cada palabra como base y comparo sus letras con las de todas las demás palabras que todavía no hayan sido agrupadas.
Para comparar, uso sorted() que ordena las letras de cada palabra 
y así puedo verificar si tienen exactamente los mismos caracteres, letra por letra.
Para no repetir palabras en varios grupos, uso una lista que marca cuáles palabras ya fueron incluidas en algún grupo. 
Si todas las letras coinciden con la palabra base, agrego esa palabra al grupo y la marco como usada.
Al final, guardo solo los grupos que tienen más de una palabra, porque esos son los que realmente comparten los mismos caracteres. 
Finalmente, muestro cada grupo en pantalla, indicando cuáles palabras tienen exactamente los mismos caracteres entre sí.
