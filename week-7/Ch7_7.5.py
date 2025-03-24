import math

def estimate_pi():
    k = 0
    total_sum = 0
    factor = 2 * math.sqrt(2) / 9801
    
    while True:
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = (math.factorial(k) ** 4) * (396 ** (4 * k))
        term = factor * (numerator / denominator)
        
        if term < 1e-15:
            break
        
        total_sum += term
        k += 1
    
    return 1 / total_sum


estimated_pi = estimate_pi()
print(f"Estimated value of pi: {estimated_pi}")
print(f"Difference from math.pi: {abs(math.pi - estimated_pi)}")