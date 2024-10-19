class Libro:
    def __init__(self, título="", género="", ISBN=""):
        self.título = título
        self.género = género
        self.ISBN = ISBN

    # Método para mostrar detalles del libro
    def mostrar_libro(self):
        return f"Título: {self.título}, Género: {self.género}, ISBN: {self.ISBN}"
        

class Autor:
    def __init__(self, nombre="", nacionalidad="", libros=None):
        if libros is None:
            libros = []
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = libros
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def borrar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print('El libro no pertenece a este autor')
        
    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        for libro in self.libros:
            print(f"  - {libro.mostrar_libro()}")
    

# Crear algunos libros
libro = Libro("El Patito Feo", "Ficción", "23262312")
libro2 = Libro("Cien Años de Soledad", "Ficción", "23262312")
libro3 = Libro("El Código Da Vinci", "Ficción", "23252312")

# Crear un autor con una lista de libros
autor1 = Autor("Mario Benedetti", "Uruguayo", [libro, libro2, libro3])

# Mostrar detalles del autor y sus libros
autor1.mostrar_autor()