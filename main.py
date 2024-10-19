import numpy as np
import sys

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        # Inicializa una matriz de adyacencia con ceros usando NumPy no se implementa funcion de agegar nodos porque se realiza con numpy
        self.matriz_adyacencia = np.zeros((num_nodos, num_nodos), dtype=int)
    
    def agregar_arista(self, origen, destino, peso):
        self.matriz_adyacencia[origen][destino] = peso

    def mostrar_matriz_adyacencia(self):
        print(self.matriz_adyacencia)

    def dijkstra(self, origen):
        distancias = np.full(self.num_nodos, sys.maxsize)  # Inicializa las distancias como infinito
        distancias[origen] = 0
        visitados = np.full(self.num_nodos, False)  # Inicializa todos los nodos como no visitados
        padre = np.full(self.num_nodos, -1)  # Para almacenar el camino

        for _ in range(self.num_nodos):
            # Selecciona el nodo con la distancia mínima que no ha sido visitado
            min_distancia = sys.maxsize
            nodo_actual = -1
            for nodo in range(self.num_nodos):
                if not visitados[nodo] and distancias[nodo] < min_distancia:
                    min_distancia = distancias[nodo]
                    nodo_actual = nodo

            # Marca el nodo actual como visitado
            visitados[nodo_actual] = True

            # Actualiza las distancias de los vecinos
            for vecino in range(self.num_nodos):
                peso = self.matriz_adyacencia[nodo_actual][vecino]
                if peso > 0 and not visitados[vecino]:  # Hay una conexión y el vecino no ha sido visitado
                    nueva_distancia = distancias[nodo_actual] + peso
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        padre[vecino] = nodo_actual

        return distancias, padre
    
    # Funcion auxiliar de Camino más corto se coupa de Imprimir el camino  
    def mostrar_camino(self, padre, destino):
        if padre[destino] == -1:
            print(destino, end=' ')
            return
        self.mostrar_camino(padre, padre[destino])
        print(destino, end=' ')

    # Imprime el camino más corto
    def camino_mas_corto(self, origen, destino):
        distancias, padre = self.dijkstra(origen)
        print(f"Distancia más corta desde {origen} a {destino}: {distancias[destino]}")
        print("Camino:", end=' ')
        self.mostrar_camino(padre, destino)
        print()
        
        
# Ejemplo de uso:
num_nodos = 5
grafo = Grafo(num_nodos)

# Agregar aristas: (origen, destino, peso)
grafo.agregar_arista(0, 1, 6)
grafo.agregar_arista(0, 3, 1)
grafo.agregar_arista(1, 3, 2)
grafo.agregar_arista(1, 2, 5)
grafo.agregar_arista(3, 2, 1)
grafo.agregar_arista(2, 4, 5)
grafo.agregar_arista(3, 4, 2)

# Mostrar la matriz de adyacencia
print("Matriz de adyacencia:")
grafo.mostrar_matriz_adyacencia()

# Aplicar el algoritmo de Dijkstra para encontrar el camino más corto
origen = 0
destino = 4
grafo.camino_mas_corto(origen, destino)