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
    
    #visitamos primero el subárbol izquierdo, luego la raíz, y finalmente el subárbol derecho.
    def recorrido_inorden(self, nodo):
        
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.derecha)
            
    
arbol = arbolBinario(1)
arbol.agregarNodo(10)
arbol.agregarNodo(5)
arbol.agregarNodo(15)
arbol.agregarNodo(2)
arbol.agregarNodo(7)

print("Recorrido inorden del árbol:")
arbol.recorrido_inorden(arbol.raiz)