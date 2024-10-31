from collections import deque

class Arbol:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def agregarElemento(self, grado, estudiantes, gradoPadre):
        # Busca el subárbol donde se agregará el nuevo nodo
        subarbol = self.buscarSubarbol(gradoPadre)
        if subarbol is not None:
            subarbol.hijos.append(Arbol(grado, estudiantes))
        else:
            print(f"No se encontró el grado {gradoPadre}.")

    def buscarSubarbol(self, grado):
        if self.grado == grado:
            return self
        for subarbol in self.hijos:
            arbolBuscado = subarbol.buscarSubarbol(grado)
            if arbolBuscado is not None:
                return arbolBuscado
        return None

    def recorrido_por_niveles(self):
        cola = deque([self])  # Inicializamos la cola con el nodo raíz

        while cola:
            nodo_actual = cola.popleft() #saca un elemento del principio
            # Imprime el grado y sus estudiantes
            print(f"Grado {nodo_actual.grado}: {', '.join(nodo_actual.estudiantes)}")

            # Añade los hijos del nodo actual a la cola
            for hijo in nodo_actual.hijos:
                cola.append(hijo)

# Ejemplo de uso
# Crear el árbol con grados y estudiantes
raiz = Arbol(12, ["Ana", "Luis"])
raiz.agregarElemento(11, ["Juan", "Maria"], 12)
raiz.agregarElemento(10, ["Pedro", "Clara"], 11)
raiz.agregarElemento(9, ["Lucas", "Elena"], 10)
raiz.agregarElemento(8, ["Sofia", "Diego"], 9)
raiz.agregarElemento(7, ["Pablo", "Raul"],8)
raiz.agregarElemento(6, ["Dario", "Lucia"], 7)
raiz.agregarElemento(5, ["Mariana", "Martin"], 6)
raiz.agregarElemento(4, ["Rodrigo", "Diego"], 5)
raiz.agregarElemento(3, ["Fabiana", "Diana"], 4)
raiz.agregarElemento(2, ["Dolores", "Paola"], 3)
raiz.agregarElemento(1, ["Sofia", "Ramiro"], 2)

# Llamar al método de recorrido por niveles
print("Recorrido por niveles:")
raiz.recorrido_por_niveles()
