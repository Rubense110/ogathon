# archivo: main.py

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Virus Propagation Challenge",
    version="1.0",
    docs_url="/swagger", 
    redoc_url=None      
)


### RETO 1
def contar_formas(distancia: int) -> int:
    if distancia == 0:
        return 1
    if distancia == 1:
        return 1

    formas = [0] * (distancia + 1)
    formas[0] = 1
    formas[1] = 1

    for i in range(2, distancia + 1):
        formas[i] = formas[i-1] + formas[i-2]

    return formas[distancia]

@app.get("/challenges/solution-1", summary="Calcula el número de patrones de propagación", response_class=JSONResponse)
def solution_1(n: int = Query(..., description="Distancia a alcanzar")):
    if n < 0:
        return JSONResponse(status_code=400, content={"error": "La distancia debe ser un número positivo o cero."})

    resultado = str(contar_formas(n))
    return resultado

### RETO 2

# Función que calcula la siguiente número en la secuencia sumando los cuadrados de los dígitos
def siguiente_numero(n):
    suma = 0
    while n > 0:
        digito = n % 10  # Obtiene el último dígito
        suma += digito * digito  # Suma el cuadrado del dígito
        n = n // 10  # Elimina el último dígito
    return suma

# Función que verifica si la secuencia de un número termina en 89
def secuencia_llega_a_89(n):
    while n != 1 and n != 89:
        n = siguiente_numero(n)  # Avanza al siguiente número en la secuencia
    return n == 89  # Devuelve True si la secuencia termina en 89

# Función que cuenta cuántos números hasta 'maximo' generan secuencias que terminan en 89
def contar_numeros_hasta(maximo):
    contador = 0
    for i in range(1, maximo + 1):
        if secuencia_llega_a_89(i):  # Si la secuencia de 'i' termina en 89, incrementamos el contador
            contador += 1
    return contador

@app.get("/challenges/solution-2", summary="Calcula el número de secuencias que terminan en 89", response_class=JSONResponse)
def solution_1(n: int = Query(..., description="Número máximo a considerar")):
    if n < 0:
        return JSONResponse(status_code=400, content={"error": "El parámetro n debe ser un número entero positivo."})

    # Llamamos a la función para calcular cuántos números hasta 'n' generan secuencias que terminan en 89
    resultado = contar_numeros_hasta(n)
    return str(resultado)


### RETO 3

# Modelo para recibir el cuerpo de la solicitud
class Residuos(BaseModel):
    residuos: List[List[int]]  # Lista de listas que representa los contenedores y residuos

# Función para calcular los movimientos necesarios
def min_movimientos(contenedores):
    # Las 6 permutaciones posibles de [0, 1, 2]
    permutaciones = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0]
    ]
    
    min_movs = float('inf')

    for asignacion in permutaciones:
        movimientos = 0
        for idx_contenedor in range(3):
            tipo_asignado = asignacion[idx_contenedor]
            for tipo in range(3):
                if tipo != tipo_asignado:
                    movimientos += contenedores[idx_contenedor][tipo]
        if movimientos < min_movs:
            min_movs = movimientos

    return min_movs

# Endpoint POST para calcular los movimientos
@app.post("/challenges/solution-3", summary="Calcula el número mínimo de movimientos de residuos")
def solution_3(residuos: List[List[int]]):
    # Llamamos a la función para calcular el número mínimo de movimientos
    movimientos = min_movimientos(residuos)
    return movimientos



"""
[
  [1, 3, 2],
  [2, 1, 3],
  [3, 2, 1]
]
"""