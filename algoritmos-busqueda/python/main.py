import csv, random, os
from time_utils import measure
from binary_search import binary_search
from ternary_search import ternary_search
from jump_search import jump_search

def load_array(path):
    with open(path, 'r') as f:
        return sorted([int(line.strip()) for line in f])

os.makedirs('../results', exist_ok=True)

sizes = [10000, 100000, 1000000]
results = []

for n in sizes:
    path = f"../data/data_{n}.txt"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}. Corra generate_data.py primero.")
    arr = load_array(path)
    target = random.choice(arr)
    print(f"\nArray size: {n}")
    t_bin = measure(binary_search, arr, target)
    t_ter = measure(ternary_search, arr, target)
    t_jump = measure(jump_search, arr, target)
    print(f"Binary: {t_bin:.3f} ms | Ternary: {t_ter:.3f} ms | Jump: {t_jump:.3f} ms")
    results.append(['Python', n, f"{t_bin:.6f}", f"{t_ter:.6f}", f"{t_jump:.6f}"])

with open('../results/results_python.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Language','Array Size','Binary','Ternary','Jump'])
    writer.writerows(results)
print('\n Resultados guardados en resultados/results_python.csv')
