# text_formatting.py


def a_negrita(texto):
    """Devuelve el texto en formato de negrita para la consola."""
    return f"\033[1m{texto}\033[0m"

def a_italica(texto):
    """Devuelve el texto en formato de cursiva para la consola."""
    return f"\033[3m{texto}\033[0m"

def subrayado(texto):
    """Devuelve el texto subrayado para la consola."""
    return f"\033[4m{texto}\033[0m"

def texto_normal(texto):
    """Devuelve el texto sin formato adicional."""
    return texto