# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    # range(1, n + 1) genera números desde el 1 hasta n
    # list() convierte ese rango en una lista real
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    # Usamos una "lista por comprensión":
    # Multiplica n por cada 'i' en el rango del 1 al 10
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    # 1. str(abs(n)) convierte el número a texto (y abs quita el signo si es negativo)
    # 2. Recorremos cada caracter (dígito), lo volvemos a convertir a entero int(d)
    # 3. sum() suma todos esos valores de la lista generada
    return sum(int(d) for d in str(abs(n)))


def es_primo(n: int) -> bool:
    # Los primos son mayores a 1
    if n < 2:
        return False
    # Verificamos si algún número desde 2 hasta la raíz cuadrada de n lo divide
    # Si el resto (%) es 0, significa que no es primo
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    # Casos base: si piden 0 o menos, lista vacía; si piden 1, solo el 0
    if n <= 0: return []
    if n == 1: return [0]
    
    # Empezamos la serie con los dos primeros valores fijos
    fib = [0, 1]
    # Usamos un bucle while para seguir agregando números hasta llegar a N
    while len(fib) < n:
        # El nuevo número es la suma de los dos últimos: [-1] y [-2]
        fib.append(fib[-1] + fib[-2])
    
    return fib