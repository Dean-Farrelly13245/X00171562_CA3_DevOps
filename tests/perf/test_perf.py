import time
from Calculator.calculator import add

def test_add_performance():
    start = time.perf_counter()

    # simple loop that simulates load
    for _ in range(50000):
        add(1, 1)

    duration = time.perf_counter() - start
    assert duration < 0.5, f"Performance too slow: {duration:.4f}s"

