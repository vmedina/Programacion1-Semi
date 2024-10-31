#Desarrolla un programa que, dado un conjunto de tres números enteros introducidos por el usuario, determine cuál de ellos es el mayor. 
#Considera la posibilidad de que algunos o todos los números sean iguales. 
#El programa debe imprimir un mensaje claro con el número mayor o indicar si todos los números son iguales.


i = 1
listaDeNumeros = []  
#solicito números menores a 4, valido que el valor ingresado sea numérico
while i < 4:
    try:
        numero=int(input("Inserte un número:"))
        listaDeNumeros.append(numero)
        i += 1
    except ValueError:
        print("Ese valor no es numérico.")
        i -= 1

# Verificar si todos los números son iguales
if listaDeNumeros[0] == listaDeNumeros[1] == listaDeNumeros[2]:
    print("Todos los números son iguales:", listaDeNumeros[0])
else:
    # Determinar el número mayor
    mayor = max(listaDeNumeros)
    print("El número mayor es:", mayor)
    
