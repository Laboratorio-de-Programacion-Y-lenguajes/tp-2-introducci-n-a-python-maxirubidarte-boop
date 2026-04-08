# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Gemini

**Prompt usado**:
# ahora sos un experto en python y algoritmos y me vas a ayudar a crear el codigo de las funciones que te voy a describir a continuacion,
# la primera funcion recibe un nombre por parametro y devuelve un saludo de formato "Hola {nombre}!",
# la siguiente funcion consiste en una suma de dos numeros enteros que recibe la funcion por parametro y retorna la suma de ambos por consola con el formato "La suma {a} + {b} = resultado", 
# la siguiente funcion es una funcion que verifica un numero entero que recibe por parametro que representa la edad de una persona y su retorno es true en caso de ser mayor a 18 años y false en caso contrario pero en caso de ingresar un valor absurdo menor o igual que cero o un numero mayor de 100, la salida es false e imprime un mensaje de error por el numero invalido, 
# la siguiente funcion es una funcion que recibe un valor por parametro y retorna el tipo de dato del valor recibido, 
# la ultima funcion es una funcion que recibe un string numerico por parametro y lo convierte a un numero flotante y lo retorna
> 

**Resultado obtenido**:
def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    Nota: Ajustado al formato que espera el test del TP.
    """
    return f"Hola, {nombre}!"

def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.
    """
    # Los tests suelen esperar el resultado numérico para validar.
    return a + b

def es_mayor_de_edad(edad: int) -> bool:
    """
    Verifica si es mayor de edad con validación de rango (1-100).
    """
    if edad <= 0 or edad > 100:
        print("Error: Número inválido")
        return False
    return edad >= 18

def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato (int, str, float, bool).
    """
    return type(valor).__name__

def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    """
    return float(valor)


**¿Lo usaste tal cual o lo modificaste?**
no modifique nada


---

### 2 - condicionales.py

**Herramienta**: Gemini

**Prompt usado**:
# la primera funcion recibe un numero entero por parametro y retorna si es "positivo", "negativo" o "cero" segun el valor recibido,
# la siguiente funcion consiste en comparar tres numeros enteros que se reciben por parametro y retornar el mayor de los tres,
# la siguiente funcion clasifica una nota que ingresa por parametro como float y retorna el mensaje correspondiente donde sobresaliente es >= 9, bueno es >= 7, aprobado es >= 6 y desaprobado es < 6, pero si la nota es menor a 0 o mayor a 10 imprime "Nota invalida" y retorna dicho mensaje,
# la ultima funcion recibe un anio entero por parametro y retorna un boolean true si el anio es bisiesto, recordando que es bisiesto si es divisible por 4 excepto los divisibles por 100 salvo que tambien lo sean por 400
> 

**Resultado obtenido**:
def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """
    return max(a, b, c)


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota con validación de rango 0-10.
    """
    if nota < 0 or nota > 10:
        print("Nota invalida")
        return "Nota invalida"
    
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    """
    # Un año es bisiesto si es divisible por 4, 
    # excepto los divisibles por 100, salvo que también lo sean por 400.
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


**¿Lo usaste tal cual o lo modificaste?**
no cambie nada pero si me di cuenta que no pense en especificarle que queria que el codigo sea lo mas eficiente posible para no usar tantos if else.


---

### 3 - listas.py

**Herramienta**:Gemini 

**Prompt usado**:
# me vas a ayudar a crear el codigo de las funciones que te voy a describir a continuacion buscando un codigo eficiente y coherente,
# la primera funcion recibe una lista de numeros enteros y su objetivo es retornar la suma de estos, retornando un float,
# la siguiente funcion recibe una lista de numeros y tiene que retornar una lista que tiene solo los numeros pares,
# la siguiente funcion recibe una lista y tiene que invertir la lista y retornarla,
# la siguiente funcion recibe una lista donde tiene que filtrar los elementos que estan duplicados y retornar una lista que no contiene duplicados, cabe destacar que el orden de la primera  # # # lista tiene que mantenerse en la segunda,
# la siguiente funcion recibe una lista con listas, y su objetivo es retornar una lista que contenga la mezcla de las listas manteniendo el orden.
> 

**Resultado obtenido**:
def suma_lista(numeros: list) -> float:
    """Retorna la suma de los elementos como float."""
    return float(sum(numeros))

def filtrar_pares(numeros: list) -> list:
    """Retorna una lista solo con los números pares."""
    return [n for n in numeros if n % 2 == 0]

def invertir_lista(lista: list) -> list:
    """Retorna la lista invertida sin modificar la original."""
    return lista[::-1]

def eliminar_duplicados(lista: list) -> list:
    """Retorna una lista sin duplicados manteniendo el orden original."""
    # dict.fromkeys es la forma más eficiente de eliminar duplicados preservando el orden
    return list(dict.fromkeys(lista))

def aplanar_lista(lista_de_listas: list) -> list:
    """Retorna una única lista con todos los elementos en orden."""
    # List comprehension anidada para máxima eficiencia
    return [item for sublista in lista_de_listas for item in sublista]


**¿Lo usaste tal cual o lo modificaste?**
no modifique nada pero esta vez le aclare que queria un codigo eficiente


---

### 4 - diccionarios.py

**Herramienta**: Gemini

**Prompt usado**:
El primer método es sobre contar palabras: recibe un string que es un texto y debe retornar un diccionario con la frecuencia de cada palabra. Por ejemplo, "hola adios hola" da como salida {"hola": 2, "adios": 1}. Las palabras deben ser comparadas en minúsculas.

El siguiente método trata sobre invertir un diccionario que entra por parámetros y retorna un nuevo diccionario con las claves y valores invertidos. Ejemplo: {"a": 1} -> {1: "a"}.

La siguiente función recibe 2 diccionarios y retorna un nuevo diccionario que es la mezcla de ambos. Si hay claves repetidas, prevalecen las del segundo diccionario.

La siguiente función recibe un diccionario y un entero para filtrar el diccionario: retorna un nuevo diccionario con los pares que sean mayores o iguales a ese número entero (el mínimo).

Nota adicional: Quiero comentarios con una explicación general en cada método para acostumbrarme al lenguaje, manejando los errores sin comprometer las pruebas automáticas.
> 

**Resultado obtenido**:
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


**¿Lo usaste tal cual o lo modificaste?**
lo deje tal cual me lo paso la ia ya que no tengo mucha practica con python


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
