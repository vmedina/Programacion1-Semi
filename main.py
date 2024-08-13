def manipula_cadena(mi_string):   
        #con split se puede corta cada palabra para generar un arreglo.
        palabras = mi_string.split()
        #la funcion capitalize() convierte en mayusucula la priemra letra de cada palabra del arreglo
        palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
        #toma todas las palabras de la lista palabras_capitalizadas, 
        # las une en un solo string con un espacio entre cada palabra, y luego devuelve ese string.
        return " ".join(palabras_capitalizadas)

#se define un string cualquiera 
mi_string = "soy un string de prueba"

#la funcion manipular cadena recibe 
nueva_cadena = manipula_cadena(mi_string)

print(nueva_cadena)
