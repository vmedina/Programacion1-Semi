class nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class arbolBinario:
    def __init__(self, valor):
        # Inicializamos la raíz con el valor dado
        self.raiz = nodo(valor)
        
    def agregarNodo(self, valor):
        
        #verificar si el árbol está vacío, en ese caso agergar el nodo a la raíz. 
        if self.raiz is None:
            self.raiz = nodo(valor)
        else:
            self.agregarNodo_recursivo(valor, self.raiz)
    
    def agregarNodo_recursivo(self, valor, nodoActual):
        
        #si el valor es menor se inserta en el lado izquierdo
        if valor < nodoActual.valor:
            if nodoActual.izquierda is None:
                nodoActual.izquierda = nodo(valor)
            else:
                self.agregarNodo_recursivo(valor, nodoActual.izquierda)
        #si el valor es mayor se inserta del lado derecho
        else:
            if nodoActual.derecha is None:
                nodoActual.derecha = nodo(valor)
            else:
                self.agregarNodo_recursivo(valor, nodoActual.derecha)
    
   
   # Método para encontrar el valor máximo en postorden
    def recorridoPostOrden(self, nodo):
        if nodo is not None:
            max_izq = self.recorridoPostOrden(nodo.izquierda)    # Recorrer subárbol izquierdo
            max_der = self.recorridoPostOrden(nodo.derecha)      # Recorrer subárbol derecho
            max_actual = nodo.valor                              # Nodo actual
            print(max_actual, end=' ')                           # Imprimir el valor del nodo
            
            # Determinar el valor máximo entre nodo actual, max_izq y max_der
            return max(max_actual, max_izq, max_der)
        else:
            return float('-inf')  # Devolver el valor mínimo si el nodo es None

            
   
    
arbol = arbolBinario(1)
arbol.agregarNodo(10)
arbol.agregarNodo(5)
arbol.agregarNodo(15)
arbol.agregarNodo(2)
arbol.agregarNodo(7)

print("Recorrido postorden del árbol y búsqueda del valor máximo:")
valor_maximo = arbol.recorridoPostOrden(arbol.raiz)
print("\nEl valor máximo del árbol es:", valor_maximo)