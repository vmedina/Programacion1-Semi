import string
import random

def generar_contraseña(longitud=12):
    # string.ascii_letters Esto incluye todas las letras del alfabeto en minúsculas y mayúsculas. 
    # Equivale a 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    # string.digits incluye todos los dígitos decimales, que son '0123456789'
    # string.punctuation 
    # incluye todos los caracteres de puntuación, tales como '!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'`.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # utilizo random.choice para seleccionar un caracter al azar con for itera la cantidad esta indicada por la variable longitud,
    # join concatena los caracteres 
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print("Su nueva contraseña es:" + generar_contraseña())