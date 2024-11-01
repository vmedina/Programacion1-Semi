#Tienes una lista ordenada alfabéticamente con los nombres de los estudiantes de una clase. 
# Implementa una función que realice una búsqueda binaria para encontrar un estudiante específico en la lista. 
#Si el estudiante no está, la función debe mostrar un mensaje adecuado.

listaDeEstudiantes = ['Pedro', 'Juan', 'Luis', 'Vanesa']

estudiantesOrdenados = sorted(listaDeEstudiantes)
print(estudiantesOrdenados)

# Búsqueda binaria de un estudiante por su nombre
def busqueda_binaria(estudiantes, estudianteABuscar):
    bajo = 0
    alto = len(estudiantes) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if estudiantes[medio] == estudianteABuscar:
            return medio  # estudiante encontrado
        elif estudiantes[medio] < estudianteABuscar:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1  # estudiante no encontrado

# Buscar el estudiante por nombre
resultado = busqueda_binaria(estudiantesOrdenados, 'Pedro')
print(f"Estudiante encontrado en la posición: {resultado}")