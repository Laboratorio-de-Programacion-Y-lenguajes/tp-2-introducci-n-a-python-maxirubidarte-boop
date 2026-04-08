# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    # Creamos una nueva lista aplicando la función 'func' a cada elemento 'x'
    # Esto es similar a lo que hace la función map() de Python
    return [func(x) for x in lista]


def componer(f, g):
    # Retornamos una nueva función (lambda) que acepta un argumento 'x'
    # Primero ejecuta g(x) y al resultado le aplica f()
    return lambda x: f(g(x))


def memoizar(func):
    # El diccionario 'cache' vivirá dentro de esta función "padre"
    cache = {}

    def interna(arg):
        # Si el argumento no está en el diccionario, lo calculamos y guardamos
        if arg not in cache:
            cache[arg] = func(arg)
        # Retornamos el valor guardado (así evitamos repetir cálculos costosos)
        return cache[arg]
    
    return interna


def reducir(lista: list, func, inicial):
    # Empezamos con el valor inicial proporcionado
    acumulado = inicial
    # Recorremos la lista y en cada paso actualizamos el acumulado
    # usando la función 'func' (que recibe el acumulado y el elemento actual)
    for elemento in lista:
        acumulado = func(acumulado, elemento)
    
    return acumulado
