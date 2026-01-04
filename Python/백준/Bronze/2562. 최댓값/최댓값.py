ns = [int(input()) for _ in range(9)]
val, idx = max((val, i) for i, val in enumerate(ns, 1))

print(val, idx, sep="\n")
