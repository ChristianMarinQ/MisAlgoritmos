import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

java_path = '../results/results_java.csv'
py_path = '../results/results_python.csv'

if not os.path.exists(java_path) or not os.path.exists(py_path):
    raise FileNotFoundError('Ejecute primero Java Main y Python main.py para generar resultados CSV.')

java = pd.read_csv(java_path)
py = pd.read_csv(py_path)

# unify column names if necessary
java.columns = ['Language','Array Size','Binary','Ternary','Jump']
py.columns = ['Language','Array Size','Binary','Ternary','Jump']

df = pd.concat([java, py])

sizes = [10000, 100000, 1000000]
algorithms = ['Binary','Ternary','Jump']

os.makedirs('../results', exist_ok=True)

for algo in algorithms:
    fig, ax = plt.subplots()
    x = np.arange(len(sizes))
    width = 0.35

    java_times = [float(java[java['Array Size']==s][algo].values[0]) for s in sizes]
    py_times = [float(py[py['Array Size']==s][algo].values[0]) for s in sizes]

    rects1 = ax.bar(x - width/2, java_times, width, label='Java')
    rects2 = ax.bar(x + width/2, py_times, width, label='Python')

    # add labels
    for i, v in enumerate(java_times):
        ax.text(i - width/2, v, f"{v:.3f}", ha='center', va='bottom', fontsize=8)
    for i, v in enumerate(py_times):
        ax.text(i + width/2, v, f"{v:.3f}", ha='center', va='bottom', fontsize=8)

    ax.set_title(f'Execution Time Comparison - {algo} Search')
    ax.set_xlabel('Array size')
    ax.set_ylabel('Time (ms)')
    ax.set_xticks(x)
    ax.set_xticklabels([str(s) for s in sizes])
    ax.legend()
    plt.tight_layout()
    out = f"../results/{algo.lower()}_comparison.png"
    fig.savefig(out)
    plt.close(fig)

print('Graficos guardados en ../results/')