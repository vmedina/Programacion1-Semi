def mostrar_prestamos():
    """Muestra todos los préstamos actuales en el archivo."""
    try:
        with open("prestamos.txt", "r") as file:
            prestamos = file.readlines()
            if not prestamos:
                print("No hay préstamos registrados.")
                return []
            print("\nPréstamos actuales:")
            for i, prestamo in enumerate(prestamos, start=1):
                print(f"{i}. {prestamo.strip()}")
            return prestamos
    except FileNotFoundError:
        print("El archivo 'prestamos.txt' no existe.")
        return []


def eliminar_prestamo():
    """Permite al usuario seleccionar y eliminar un préstamo del archivo."""
    prestamos = mostrar_prestamos()
    if not prestamos:
        return  # No hay préstamos para eliminar

    try:
        index = int(input("\nSeleccione el número del préstamo que desea eliminar: "))
        if 1 <= index <= len(prestamos):
            prestamos.pop(index - 1)
            with open("prestamos.txt", "w") as file:
                file.writelines(prestamos)
            print("\nPréstamo eliminado con éxito.")
        else:
            print("Número inválido. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")


# Ejecución principal
if __name__ == "__main__":
    eliminar_prestamo()
