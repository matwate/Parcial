# La función contains_loop toma un nombre de archivo y devuelve True si los datos en el archivo contienen un ciclo.
# Un ciclo es una secuencia de amigos que eventualmente lleva de vuelta al amigo original.
def contains_loop(file_name: str) -> bool:
    # Creamos un diccionario vacío para almacenar los amigos.
    friends = {}
    # Abrimos el archivo en modo lectura.
    with open(file_name, "r") as f:
        # Leemos todas las líneas del archivo.
        data = f.readlines()
        # Dividimos cada línea en dos partes y las almacenamos como una lista de listas.
        data = [line.strip().split() for line in data]
    # Para cada amigo en los datos, añadimos el amigo y su amigo correspondiente al diccionario.
    for friend in data:
        friends[friend[0]] = friend[1]
    # Para cada amigo en el diccionario, verificamos si hay un ciclo.
    for friend in friends:
        # Creamos un conjunto vacío para almacenar los amigos visitados.
        visited = set()
        # Establecemos el amigo actual como el amigo que estamos verificando.
        current = friend
        # Mientras el amigo actual no haya sido visitado, continuamos el ciclo.
        while current not in visited:
            # Añadimos el amigo actual al conjunto de amigos visitados.
            visited.add(current)
            # Establecemos el amigo actual como el amigo del amigo actual.
            current = friends.get(current)
            # Si el amigo actual es el amigo que estamos verificando, hemos encontrado un ciclo y devolvemos True.
            if current == friend:
                return True
    # Si hemos verificado todos los amigos y no hemos encontrado un ciclo, devolvemos False.
    return False

# Imprimimos el resultado de la función para tres archivos diferentes.
print(contains_loop("data.txt"))  # Debería imprimir True si "data.txt" contiene un ciclo, False en caso contrario.
print(contains_loop("noloops.txt"))  # Debería imprimir True si "noloops.txt" contiene un ciclo, False en caso contrario.
print(contains_loop("loveyourself.txt"))  # Debería imprimir True si "loveyourself.txt" contiene un ciclo, False en caso contrario.