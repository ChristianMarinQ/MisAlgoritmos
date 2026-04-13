import random, os

def generate_data():
    os.makedirs('../data', exist_ok=True)
    sizes = [10000, 100000, 1000000]
    for n in sizes:
        path = f"../data/data_{n}.txt"
        if os.path.exists(path):
            print(f"{path} already exists, skipping.")
            continue
        print(f"Generating {path} ({n} numbers)... This can take a while for 1,000,000 elements.")
        with open(path, 'w') as f:
            for _ in range(n):
                f.write(str(random.randint(10_000_000, 99_999_999)) + '\n')

if __name__ == '__main__':
    generate_data()
