input()
print(sum((ord(x) - 96) * 31**i for i, x in enumerate(input())) % 1234567891)
