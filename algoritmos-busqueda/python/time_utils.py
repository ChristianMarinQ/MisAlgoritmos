import time
def measure(func, *args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) * 1000.0  # milliseconds
