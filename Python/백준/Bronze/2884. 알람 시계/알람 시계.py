h, m = map(int, input().split())

total_minutes = (h * 60 + m - 45) % 1440

print(total_minutes // 60, total_minutes % 60)
