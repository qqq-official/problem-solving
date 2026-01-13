n = int(input())
s = list(map(int, input().split()))
print(sum(s) * 100 / max(s) / n)
