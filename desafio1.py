inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]



#Pregunta 2: qué producto esta en la tercera posición
#Inventario es una lista, donde cada elemento tiene una posición, o índice, 
#que comienza desde 0 para el primer elemento, 1 para el segundo, y así sucesivamente.
#La expresión inventario[2] accede al elemento que está en la tercera posición de la lista 
producto_tercera_posicion = inventario[2]
print("El producto que se encuentra en la tercera posición es: ", producto_tercera_posicion)


#Pregunta 4, Como añadirías estos productos al inventiro, "frutilla", "apio", "papas"
# El método append() se usa para agregar un nuevo elemento al final de una lista ya creada. 
inventario.append("frutillas")
inventario.append("apio")
inventario.append("papas")
print("Se han incorporado tres productos al inventrio", inventario)



