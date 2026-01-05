target = str(int(input()) * int(input()) * int(input()))
counts = [0] * 10

for n in target:
    counts[int(n)] += 1

print(*counts, sep="\n")

# NOTE: count() 함수를 사용하는 방식은 비효율적이므로 지양할 것.
