# Definimos la clase base Autor
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        
# Creamos una subclase Escritor que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, poesia):
        super().__init__(nombre)
        self.poesia = poesia
        
# Instanciamos un objeto de la clase Escritor
escritor = Poeta("Mario Benedetti", "Corazón Coraza")
print(escritor.nombre, escritor.poesia)