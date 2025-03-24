import math

def square_root(a):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 1e-10:
            return y
        x = y

def test_square_root():
    print(f"{'a':<5} {'sqrt(a)':<15} {'math.sqrt(a)':<15} {'diff':<15}")
    for a in range(1, 10):
        sqrt_a = square_root(a)
        math_sqrt_a = math.sqrt(a)
        diff = abs(sqrt_a - math_sqrt_a)
        print(f"{a:<5} {sqrt_a:<15} {math_sqrt_a:<15} {diff:<15}")

test_square_root()