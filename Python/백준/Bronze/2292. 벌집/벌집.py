import math

print(math.ceil((3 + (12 * int(input()) - 3) ** 0.5) / 6))

# NOTE-1: 시간복잡도를 개선하기 위해 반복문 대신 다각수 및 계차수열 개념을 활용할 수 있음
# NOTE-2: 부동소수점 오차를 개선하기 위해 math.isqrt()를 고려할 수 있음
