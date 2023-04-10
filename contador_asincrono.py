import asyncio
import time
import os

FILE = os.path.split(os.path.join("script.py", 'contador_asíncrono.py'))[1]

async def contador():
    print("Uno")
    await asyncio.sleep(1)
    print("Dos")

async def main():
    await asyncio.gather(contador(), contador(), contador())

if __name__ == "__main__":
    s = time.perf_counter() # Establece el tiempo en el que se ejecuta cada linea de código
    asyncio.run(main())
    tiempo = time.perf_counter() - s # Establece el tiempo total de ejecución de todo el código, pero para obtener el tiempo de ejecución real debemos restastarle el tiempo de ejecución de cada linea de código
    print("El archivo {} ha sido ejecutado en {:0.2f} segundos.".format(FILE, tiempo))