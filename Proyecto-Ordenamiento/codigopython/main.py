import time, csv, os
from algoritmos_ordenamiento import shaker_sort, dual_pivot_quick_sort, heap_sort, merge_sort, radix_sort

def leer_datos(ruta, n):
    with open(ruta) as f:
        return [int(next(f)) for _ in range(n)]

def guardar_resultado(archivo, algoritmo, n, tiempo):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    with open(archivo, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([algoritmo, "Python", n, tiempo])

if __name__ == "__main__":
    archivo_datos = "../Proyecto-Ordenamiento/datos/datos.txt"
    archivo_resultados = "../Proyecto-Ordenamiento/resultados/resultados_python.csv"
    tamanos = [10_000, 100_000, 1_000_000]
    algoritmos = {
        #"Shaker": shaker_sort,
        "DualPivotQuickSort": dual_pivot_quick_sort,
        "Heap": heap_sort,
        "Merge": merge_sort,
        "Radix": radix_sort
    }

    for n in tamanos:
        datos = leer_datos(archivo_datos, n)
        for nombre, funcion in algoritmos.items():
            copia = datos.copy()
            inicio = time.perf_counter()
            funcion(copia)
            fin = time.perf_counter()
            tiempo = fin - inicio
            guardar_resultado(archivo_resultados, nombre, n, tiempo)
            print(f"{nombre} ({n}): {tiempo:.3f} s")

    print(f"Resultados guardados en {archivo_resultados}")
