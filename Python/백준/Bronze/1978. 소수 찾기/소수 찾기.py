_ = input()
ns = map(int, input().split())

print(sum(all(x % i for i in range(2, int(x**0.5) + 1)) and x > 1 for x in ns))
