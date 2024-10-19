class Biblioteca:
    def __init__(self, nombre, libros=None):
        if libros is None:
            libros = []
        self.libros = libros
        self.nombre = nombre

    # Método para mostrar los detalles de la biblioteca
    def mostrar_biblioteca(self):
        print(f"Nombre: {self.nombre}")
        print("Libros:")
        for libro in self.libros:
            print(f"  - {libro.mostrar_libro()}")
    
    # Método para buscar un libro por título
    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.título.lower() == titulo.lower()]
        return resultados

    # Método para buscar libros por autor
    def buscar_libros_por_autor(self, autor_nombre):
        resultados = [libro for libro in self.libros if libro.autor and libro.autor.nombre.lower() == autor_nombre.lower()]
        return resultados


class Libro:
    def __init__(self, título="", género="", ISBN="", autor=None):
        self.título = título
        self.género = género
        self.ISBN = ISBN
        self.autor = autor

    # Método para mostrar detalles del libro
    def mostrar_libro(self):
        return f"Título: {self.título}, Género: {self.género}, ISBN: {self.ISBN}, Autor: {self.autor.nombre if self.autor else 'Desconocido'}"
    

class Autor:
    def __init__(self, nombre="", nacionalidad=""):        
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        

# Crear algunos autores
autor1 = Autor("Mario Benedetti", "Uruguayo")
autor2 = Autor("Onetti", "Uruguayo")
autor3 = Autor("García Márquez", "Colombiano")

# Crear algunos libros
libro = Libro("La tregua", "Ficción", "23262312", autor1)
libro2 = Libro("Cien Años de Soledad", "Ficción", "23262312", autor3)
libro3 = Libro("La vida breve", "Ficción", "23252312", autor2)

# Crear una lista de libros
listaLibros = [libro, libro2, libro3]