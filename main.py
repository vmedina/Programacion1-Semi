
# Crea una excepción personalizada llamada NegativeNumberError que se dispare si el usuario intenta 
# ingresar un número negativo en un programa de cálculo de raíces cuadradas. 
# Implementa el manejo de esta excepción en el programa.


# Definimos una excepción personalizada
class NegativeNumberError(Exception):
    """Excepción lanzada cuando se ingresa un número negativo para el cálculo del raíces cuadradas."""
    def __init__(self, numero, mensaje="El número no puede ser negativo para el cálculo del raíces cuadradas"):
        self.numero = numero
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f"{self.mensaje}. Número ingresado: {self.numero}"

# Función que calcula el raiz_Cuadrada y utiliza la excepción personalizada
import math

def calcular_raiz_Cuadrada_personalizado(numero):
    try:
        # Verifica si el número es negativo
        if numero < 0:
            raise NegativeNumberError(numero)
        
        # Calcula el raiz_Cuadrada usando la biblioteca math
        resultado = math.sqrt(numero)
        print(f"El raiz_Cuadrada de {numero} es: {resultado}")

    except NegativeNumberError as nne:
        print(f"Error: {nne}")
    except ValueError:
        print("Error de valor: El número ingresado debe ser un entero.")
    except OverflowError:
        print("Error: El número es demasiado grande para ser procesado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso del programa
try:
    numero = int(input("Ingresa un número entero positivo para calcular su raiz cuadrada: "))
    calcular_raiz_Cuadrada_personalizado(numero)
except NegativeNumberError:
    print("Error: Por favor, ingresa un número entero válido.")
