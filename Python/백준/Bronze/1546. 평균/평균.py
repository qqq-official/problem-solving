input()

ns = list(map(int, input().split()))
print(sum(map(lambda x: x / max(ns) * 100, ns)) / len(ns))
