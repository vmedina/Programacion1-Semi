class Musico:
    def instrumento(self):
        print(f"El músico toca un instrumento")

# Se crea la subclase Guitarrista, que hereda de Musico y redefine el método instrumento
class Guitarrista(Musico):
    def instrumento(self):
        print(f"El guitarrista toca la guitarra")

# Se crea la subclase Baterista, que hereda de Musico y redefine el método instrumento
class Baterista(Musico):
    def instrumento(self):
        print(f"El baterista toca la batería")

# Se instancia un objeto de cada clase
musicoUno = Musico()
guitarristaUno = Guitarrista()
bateristaUno = Baterista()

# Se guardan los objetos en una lista y se usa para mostrar el polimorfismo con un bucle for
musicos = [musicoUno, guitarristaUno, bateristaUno]
for musico in musicos:
    musico.instrumento()