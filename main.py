def realizar_operaciones(lista):
    try:
        # Solicita al usuario que elija una operación
        print("Operaciones disponibles: suma, resta, multiplicación, división")
        operacion = input("Elige una operación: ").strip().lower()

        # Verifica si la lista está vacía
        if not lista:
            raise ValueError("La lista está vacía, no se pueden realizar operaciones.")

        # Convierte los elementos de la lista a floats (manejo de ValueError)
        numeros = [float(valor) for valor in lista]

        # Realiza la operación seleccionada
        if operacion == 'suma':
            resultado = sum(numeros)
        elif operacion == 'resta':
            resultado = numeros[0]
            for num in numeros[1:]:
                resultado -= num
        elif operacion == 'multiplicación':
            resultado = 1
            for num in numeros:
                resultado *= num
        elif operacion == 'división':
            resultado = numeros[0]
            for num in numeros[1:]:
                if num == 0:
                    raise ZeroDivisionError("Intento de dividir por cero.")
                resultado /= num
        else:
            raise ValueError("Operación no válida. Debes elegir entre suma, resta, multiplicación o división.")

        print(f"El resultado de la {operacion} es: {resultado}")

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except TypeError as te:
        print(f"Error de tipo: {te}")
    except ZeroDivisionError as zde:
        print(f"Error de división: {zde}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso del programa
valores = ["10", "5", "2"]  # Lista de valores de ejemplo (pueden ser cadenas o números)
realizar_operaciones(valores)