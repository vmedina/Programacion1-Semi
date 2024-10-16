class Autor:
    def __init__(self, nombre="", nacionalidad="", libros=[]):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = libros
        
    def agregarLibro(self, libro):
        self.libros.append(libro)
        
    def borrarLibro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print('El libro no pertenece a este autor')
        
# Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        
        
autor1 = Autor("Mario Benedetti", "Uruguayo", ['Cien años de Soledad', 'El Principito'])

autor1.agregarLibro('El patito feo')

print(autor1.nombre)
print(autor1.nacionalidad)
print(autor1.libros)

autor1.borrarLibro('El Principito')
print(autor1.libros)