#Tienes una lista de números en la que algunos elementos están repetidos. 
#Desarrolla un programa que elimine todos los elementos duplicados y deje únicamente una aparición de cada uno. 
#La salida debe mostrar la lista original y la lista sin duplicados.


# Lista con duplicados
lista = [1, 2, 2, 3, 4, 4, 5]

# Eliminar duplicados convirtiendo a conjunto(set) y de vuelta a lista
# Los elementos de un set son único
lista_sin_duplicados = list(set(lista))

print("Lista sin duplicados:", lista_sin_duplicados)