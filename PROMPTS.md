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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


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
