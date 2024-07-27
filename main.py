
DIMENSIONESTABLERO =5
DISPAROS=10
CANTIDADBARCOS=3
TIPOBARCOS= [1]
JUGADORES = "UNO" # DOS O MAQUINA

tablero = [["O" for _ in range(DIMENSIONESTABLERO)] for _ in range(DIMENSIONESTABLERO)]


def colocar_barco(tablero, tamanio):
    pass
    
    
     

def hacer_tiro(tablero, fila, columna):
    # Verificar si el tiro es un hit o miss y actualizar el tablero
    pass

def verificar_victoria(tablero):
    # Comprobar si hay barcos restantes
    pass

def mostrar_tablero(tablero):
    print("La matriz es la siguiente:")
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

def juego():
    # Inicializar tablero y barcos
    # Bucle principal del juego
    while True:
       mostrar_tablero(tablero)
        # Pedir tiro al jugador
        # Comprobar si el juego ha terminado
       
    

   
colocar_barco(tablero, 3)