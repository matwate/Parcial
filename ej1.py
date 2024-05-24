# La función interleave_strings toma dos listas de cadenas y las entrelaza.
# Si una lista es más larga que la otra, los elementos restantes se añaden al final.
def interleave_strings(list1: list[str], list2: list[str]) -> list[str]:
    output = []  # Creamos una lista vacía para almacenar el resultado.
    # Iteramos sobre el rango del tamaño de la lista más pequeña.
    for _ in range(min(len(list1), len(list2))):
        # Añadimos el primer elemento de cada lista a la lista de salida.
        output.extend([list1[0], list2[0]])
        # Eliminamos el primer elemento de cada lista.
        list1.pop(0)
        list2.pop(0)
    # Si quedan elementos en la lista1, los añadimos al final de la lista de salida.
    if len(list1)>= 0:
        output.extend(list1)
    # Si quedan elementos en la lista2, los añadimos al final de la lista de salida.
    elif len(list2) >=0:
        output.extend(list2)
    # Si no quedan elementos en ninguna de las listas, no hacemos nada.
    else:
        pass
    # Devolvemos la lista de salida.
    return output


# Creamos dos listas de prueba.
a = ["a","b","c","d","e"]
b = ["1", "2", "3"]

# Imprimimos los resultados de las dos funciones.
print(interleave_strings(a,b))  # Debería imprimir: ['a', '1', 'b', '2', 'c', '3', 'd', 'e']
