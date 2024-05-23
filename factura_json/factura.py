import json
#use __init__.py para poder importar mi archivo json, 
#sirve para que Python identifique a la carpeta que lo contiene como un directorio de paquetes de Python.
#De tal manera que podamos importar los módulos que contiene esa carpeta

#genero el encabezado de la factura
print("\tNombre\t\t|Cantidad\t|Total")
print("----------------------------------------------")


# Leo el archivo JSON que contiene el listado de productos
with open('productos.json', 'r') as a_productos:
    productos = json.load(a_productos)
    #inicializo el total en 0
    suma_total = 0
    #recorro el listado de productos 
    for producto in productos:
        #calculo el total cantidad * precio
        total = int(producto['cantidad'])*float(producto['precio'])
        #imprimo los datos 
        print(f"\t{producto['nombre']}\t{producto['cantidad']}\t{producto['precio']}")

# Calculo la suma total de productos 
suma_total += total

# imprimo el total de los articulos
print("----------------------------------------------")
print("Total:                              ", suma_total)