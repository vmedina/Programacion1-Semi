#Dado un conjunto de estudiantes y sus promedios, implementa una función que cree un árbol binario de búsqueda en 
#el que los nodos representan los promedios de los estudiantes. 
#Luego, implementa una función que recorra el árbol en inorden para mostrar los estudiantes en orden ascendente de rendimiento académico.

class Nodo:
    def __init__(self, promedio, nombre):
        self.izq = None
        self.der = None
        self.promedio = promedio
        self.nombre = nombre

# Función para insertar un nuevo nodo en el árbol binario de búsqueda
def insertar(raiz, promedio, nombre):
    # Si el árbol está vacío, crea un nuevo nodo y lo devuelve
    if raiz is None:
        return Nodo(promedio, nombre)
    
    # Si el promedio es menor que el nodo actual, ve a la izquierda
    if promedio < raiz.promedio:
        raiz.izq = insertar(raiz.izq, promedio, nombre)
    else:  # Si el promedio es mayor o igual, ve a la derecha
        raiz.der = insertar(raiz.der, promedio, nombre)
    
    return raiz

# Función que recorre el árbol en inorden y muestra los estudiantes en orden ascendente de promedio
def mostrar_en_orden(raiz):
    if raiz:
        mostrar_en_orden(raiz.izq)
        print(f"{raiz.nombre}: {raiz.promedio}")
        mostrar_en_orden(raiz.der)


# Lista de estudiantes con sus promedios
estudiantes = [
    ("Juan", 85),
    ("Ana", 90),
    ("Luis", 78),
    ("Maria", 92),
    ("Carlos", 88)
]

# Se crea el árbol de búsqueda binario
raiz = None
for nombre, promedio in estudiantes:
    raiz = insertar(raiz, promedio, nombre)

# Mostrar los estudiantes en orden ascendente de promedio
print("Estudiantes en orden ascendente de promedio:")
mostrar_en_orden(raiz)