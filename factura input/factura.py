#inicializamos variables que seran usadas posteriormente en el algoritmo
continuar = True
total = 0
impresion = f"Descripción | Cantidad | Precio Unitario |Importe \n"

#Dado que son varios los productos que hay que agregar voy a usar un bucle while. 
#esta estructura se ejectuara mientras la condicion evaluada sea verdadera. 
#se ha incializado como True para que se ejecute al menos una vez

while continuar:
    #solicito la informacion de los productos 
    nombre= input("Ingrese el nombre del producto:")
    cantidad =input("Ingrese la cantidad:")
    precio = input("Ingrese el precio:")
    
    #pregunto si desea agregar otro producto
    otroProducto  = input("Desea ingersar otro producto? Si / No ")
    
    #calculo el importe multiplicando la cantidad por el precio, los inputs se castean a integer y float
    importe = int(cantidad) * float(precio) 
    
    #sumo total + importe para calcular el total general  
    total = total + importe
    
    #concateno la primera linea de la factura el header con el resto de las filas que se vayan a agregar
    impresion = impresion + f" {nombre}   |    {cantidad}    |     {precio}     |   {importe} \n"
    
    if otroProducto =="No" or otroProducto == "no":
        #si no quiere agregar mas productos salgo del bucle
        continuar = False
        

#imprimo la factura Encabezado mas filas agregadas
print (impresion)
#imprimo el total general
print('Total %5.2f.' % total)


  