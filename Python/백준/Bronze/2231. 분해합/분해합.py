n_str = input()
n = int(n_str)
start = max(1, n - len(n_str) * 9)
result = 0

for i in range(start, n):
    if i + sum(map(int, str(i))) == n:
        result = i
        break

print(result)