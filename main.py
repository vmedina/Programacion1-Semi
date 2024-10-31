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
    
   
   # Método para realizar la búsqueda binaria en el árbol
    def buscar(self, valor, nodo):
        if nodo is None:
            return False  # Si llegamos a un nodo nulo, el valor no está en el árbol
        if nodo.valor == valor:
            return True  # Valor encontrado
        elif valor < nodo.valor:
            return self.buscar(valor, nodo.izquierda)  # Buscar en el subárbol izquierdo
        else:
            return self.buscar(valor, nodo.derecha)    # Buscar en el subárbol derecho

            
   
    
arbol = arbolBinario(1)
arbol.agregarNodo(10)
arbol.agregarNodo(5)
arbol.agregarNodo(15)
arbol.agregarNodo(2)
arbol.agregarNodo(7)


# Buscar valores en el árbol
valor_a_buscar = 7
encontrado = arbol.buscar(valor_a_buscar, arbol.raiz)
print(f"El valor {valor_a_buscar} {'fue encontrado' if encontrado else 'no fue encontrado'} en el árbol.")

valor_a_buscar = 8
encontrado = arbol.buscar(valor_a_buscar, arbol.raiz)
print(f"El valor {valor_a_buscar} {'fue encontrado' if encontrado else 'no fue encontrado'} en el árbol.")