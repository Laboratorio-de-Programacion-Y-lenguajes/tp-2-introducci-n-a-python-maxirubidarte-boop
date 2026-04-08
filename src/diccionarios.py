# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    # 1. Convertimos todo a minúsculas para que 'Hola' y 'hola' sean lo mismo
    # 2. .split() corta el texto por los espacios y nos da una lista de palabras
    palabras = texto.lower().split()
    frecuencia = {}
    
    for p in palabras:
        # .get(p, 0) busca la palabra: si existe, trae el número; si no, trae 0
        # Luego le sumamos 1 y lo guardamos
        frecuencia[p] = frecuencia.get(p, 0) + 1
        
    return frecuencia


def invertir_diccionario(d: dict) -> dict:
    # Usamos "diccionario por comprensión", una forma rápida de crear diccionarios en Python
    # Recorremos items() que nos da la (clave, valor) y los guardamos al revés (v: k)
    if not d: return {}  # Manejo básico: si está vacío, devuelve vacío
    return {v: k for k, v in d.items()}


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    # Creamos una copia del primero para no modificar el original (buena práctica)
    resultado = d1.copy()
    # .update() agrega lo de d2; si una clave ya existe, la reemplaza con el valor de d2
    resultado.update(d2)
    return resultado


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    # Filtramos usando otra comprensión de diccionario
    # "Manteneme k:v SOLO SI v es mayor o igual al minimo"
    return {k: v for k, v in d.items() if v >= minimo}
