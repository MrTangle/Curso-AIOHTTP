import time
import os

FILE = os.path.split(os.path.join("script.py", 'contador_no_asíncrono.py'))[1]

def contador():
    print("Uno")
    time.sleep(1)
    print("Dos")

def principal():
    for _ in range(3): # Ejecutamos 3 veces la función al igual que en el ejemplo asíncrono para que haya similitud
        contador()

if __name__ == "__main__":
    s = time.perf_counter()
    principal()
    tiempo = time.perf_counter() - s
    print("El archivo {} ha sido ejecutado en {:0.2f} segundos.".format(FILE, tiempo))