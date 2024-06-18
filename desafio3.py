#ejemplo de codigos ascii 65, 66, 67, 68, 69, 97, 98, 99, 100, 101
#recibo por input una lista de enteros
caracterIngresado =input("Ingrese la lista de numeros ascii separados por , para ver su caracter:")
#con el metodo split corto la lista por la coma
arregloDeCaracteres = caracterIngresado.split(",")


for numero in arregloDeCaracteres:
    # chr es una función que se utiliza para convertir un entero que 
    # representa un valor ASCII o Unicode en su correspondiente carácter
    caracter  = chr(int(numero))
    print(f"{numero} -> {caracter}")
    
