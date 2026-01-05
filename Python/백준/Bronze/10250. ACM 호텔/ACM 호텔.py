for _ in range(int(input())):
    h, w, n = map(int, input().split())

    floor = (n - 1) % h + 1
    room = (n - 1) // h + 1

    print(f"{floor}{room:02d}")
