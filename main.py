import math

def calcular_factorial():
    try:
        # Solicita al usuario que ingrese un número
        numero = input("Ingresa un número entero positivo para calcular su factorial: ")
        
        # Intenta convertir el número a un entero
        numero = int(numero)
        
        # Verifica si el número es negativo
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        
        # Calcula el factorial usando la biblioteca math
        resultado = math.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except OverflowError:
        print("Error: El número es demasiado grande para ser procesado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso del programa
calcular_factorial()