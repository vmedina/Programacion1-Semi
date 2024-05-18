#entrada de datos 
primerNumero = float(input("Ingrese el primer numero:"))
segundoNumero = float(input("Ingrese el segundo numero:"))

#realizo los calculos de la calculadora 
suma = primerNumero + segundoNumero
resta = primerNumero - segundoNumero
multiplicacion = primerNumero * segundoNumero
division = primerNumero / segundoNumero

#uso %5.2f para formatear la salida del float a dos digitos 
#imprimo los resultados
print ("---------------Caclucladora Simple-------------------------")
print ("El resultado de la suma es : %5.2f" % suma)
print ("El resultado de la resta es : %5.2f" % resta)
print ("El resultado de la multiplicación es : %5.2f" % multiplicacion)
print ("El resultado de la suma división es :  %5.2f" % division)
print ("----------------------------------------------------------")



