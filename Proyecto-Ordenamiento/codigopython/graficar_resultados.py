import pandas as pd
import matplotlib.pyplot as plt
import os

ruta_java = "../Proyecto-Ordenamiento/resultados/resultados_java.csv"
ruta_py = "../Proyecto-Ordenamiento/resultados/resultados_python.csv"

df_java = pd.read_csv(ruta_java, names=["Algoritmo", "Lenguaje", "Tamaño", "Tiempo"])
df_py = pd.read_csv(ruta_py, names=["Algoritmo", "Lenguaje", "Tamaño", "Tiempo"])

df = pd.concat([df_java, df_py])

os.makedirs("../Proyecto-Ordenamiento/resultados", exist_ok=True)

for n in df["Tamaño"].unique():
    subset = df[df["Tamaño"] == n]
    pivot = subset.pivot(index="Algoritmo", columns="Lenguaje", values="Tiempo")

    ax = pivot.plot(kind="bar", figsize=(9, 5), title=f"Tiempos de ejecución (n={n})", ylabel="Tiempo (s)", rot=0)
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2, p.get_height(),
                f"{p.get_height():.3f}", ha="center", va="bottom", fontsize=8)
    plt.tight_layout()
    plt.savefig(f"../Proyecto-Ordenamiento/resultados/grafico_{n}.png")
    plt.show()
