import math
import heapq
from collections import defaultdict

def is_perfect_square(x):
    s = math.isqrt(x)
    return s * s == x

def min_cost_to_square(x):
    s = math.isqrt(x)
    lower_sq = s * s
    upper_sq = (s + 1) * (s + 1)
    return min(x - lower_sq, upper_sq - x)

def min_operations_to_squares():
    n = int(input())
    a = list(map(int, input().split()))
    
    squares = []
    non_squares = []
    
    for num in a:
        if is_perfect_square(num):
            squares.append(num)
        else:
            non_squares.append(num)
    
    k = n // 2
    operations = 0
    
    # Якщо квадратів більше ніж потрібно
    if len(squares) > k:
        squares.sort()
        excess = len(squares) - k
        for i in range(excess):
            num = squares[i]
            if num == 0:
                operations += 2  # 0 → 1 → 2 (2 операції)
            else:
                operations += 1   # Квадрат → не квадрат (1 операція)
    
    # Якщо квадратів менше ніж потрібно
    elif len(squares) < k:
        costs = []
        for num in non_squares:
            cost = min_cost_to_square(num)
            heapq.heappush(costs, cost)
        
        needed = k - len(squares)
        for _ in range(needed):
            operations += heapq.heappop(costs)
    
    print(operations)

if __name__ == "__main__":
    min_operations_to_squares()