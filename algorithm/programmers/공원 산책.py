def solution(park, routes):
    pos = divmod(''.join(park).index('S'), len(park))
    print()

    for dir, step in [t.split() for t in routes]:
        [(1, 0), (-1, 0), (0, 1), (0, -1)][['E', 'W', 'S', 'N'].index(dir)]

solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])