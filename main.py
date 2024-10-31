#Un sistema de inventario tiene una lista con los códigos de productos. 
#Desarrolla un programa que permita al usuario introducir un código de producto y que determine si ese código está en la lista. 
#Si el código se encuentra, el programa debe devolver la posición en la que aparece; 
#si no está, debe mostrar un mensaje indicando que no se ha encontrado el código.



listaDeCodigosDeProductos = [222, 123, 678]  
def buscarCodigo(codigo):   

    # Verificación si el valor está en la lista
    if codigo in listaDeCodigosDeProductos:
        print(f"El código {codigo} está en la lista.")
    else:
        print(f"El código ingresado {codigo} no existe en nuestra lista.")

#solicito el código numérico, valido que el valor ingresado sea un número
try:
    codigo=int(input("Inserte el código que desea buscar:"))   
    buscarCodigo(codigo)
except ValueError:
    print("Ese valor no es numérico.")
   

    
