# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    # 1. Limpiamos el texto: quitamos espacios y pasamos a minúsculas
    texto_limpio = texto.replace(" ", "").lower()
    # 2. Comparamos el texto con su versión invertida [::-1]
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    # El método .title() de Python pone en mayúscula la primera letra de cada palabra
    return texto.title()


def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    # Convertimos a minúsculas y sumamos 1 por cada caracter que esté en 'vocales'
    return sum(1 for letra in texto.lower() if letra in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    resultado = ""
    for char in texto:
        # Verificamos si es una letra
        if char.isalpha():
            # Determinamos si empezamos desde 'A' o 'a' según sea mayúscula o minúscula
            inicio = ord('A') if char.isupper() else ord('a')
            # 1. Obtenemos la posición de la letra (0-25)
            # 2. Aplicamos el desplazamiento y usamos módulo 26 para "dar la vuelta" al abecedario
            # 3. Convertimos de nuevo a caracter
            nuevo_char = chr((ord(char) - inicio + desplazamiento) % 26 + inicio)
            resultado += nuevo_char
        else:
            # Si no es letra (espacios, números, puntos), queda igual
            resultado += char
    return resultado
