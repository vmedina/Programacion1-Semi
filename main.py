# main.py

# Importar funciones del módulo text_formatting
from text_formating import a_negrita, a_italica, subrayado, texto_normal

# Texto de ejemplo
texto = "Hola Mundo"

# Aplicar formatos
texto_negrita = a_negrita(texto)
texto_italica = a_italica(texto)
texto_subrayado = subrayado(texto)
texto_sin_formato = texto_normal(texto)

# Imprimir resultados
print("Texto en negrita:", texto_negrita)
print("Texto en cursiva:", texto_italica)
print("Texto subrayado:", texto_subrayado)
print("Texto normal:", texto_sin_formato)
