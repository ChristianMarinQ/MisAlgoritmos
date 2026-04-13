import random
import os

def generar_datos(cantidad, ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w") as f:
        for _ in range(cantidad):
            numero = random.randint(10_000_000, 99_999_999)
            f.write(str(numero) + "\n")

ruta = "../Proyecto-Ordenamiento/datos/datos.txt"
generar_datos(1_000_000, ruta)
print(f"Archivo generado en: {ruta}")