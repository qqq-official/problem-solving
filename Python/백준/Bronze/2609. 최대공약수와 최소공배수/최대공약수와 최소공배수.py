import math

a, b = map(int, input().split())

print(f"{math.gcd(a, b)} {math.lcm(a, b)}")
