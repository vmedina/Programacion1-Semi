#Solicita al usuario dos números enteros e implementa un try-except que maneje la división por cero y los valores no numéricos. 
# Muestra mensajes de error apropiados en cada caso.



# Intentamos realizar la división
try:
    # Solicitamos al usuario el dividendo y lo convertimos a entero
    a = int(input("Ingrese un número entero: "))

    # Solicitamos al usuario el divisor y lo convertimos a entero
    b = int(input("Ingrese otro número entero: "))
    resultado = a/b
    print(resultado)
except ValueError:
    print("Error: El valor ingresado no es un número entero.")
except TypeError:
    print("Error: Los valores permitidos son números enteros")
except ZeroDivisionError:  # Si ocurre una división por cero
    print("Error: División por cero no permitida.")
