# archivo: main.py

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

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

    resultado = contar_formas(n)
    return {"distancia": n, "patrones": resultado}

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
    return {"n": n, "result": resultado}