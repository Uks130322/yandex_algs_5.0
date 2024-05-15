"""Task H
Need to refactor but work right"""


def run(L: int, x1: int, v1: int, x2: int, v2: int):
    if x1 == x2 or (x1 + x2) / 2 == L / 2:
        print('YES')
        print(0.0)
        return

    if v1 == v2 == 0:
        print('NO')
        return

    if v1 == -v2:
        if x1 < x2:
            t = abs((L - x2 + x1))/(abs(v1) + abs(v2))
        else:
            t = abs((L + x2 - x1)) / (abs(v1) + abs(v2))
        print('YES')
        print(t)
        return

    if v1 == v2:
        if (x1 + x2) / 2 < L / 2:
            if v1 > 0:
                t = abs((L - (x1 + x2)) / (v1 + v2))
            else:
                t = abs((x1 + x2) / (v1 + v2))
        else:
            if v1 > 0:
                t = abs((2 * L - (x1 + x2)) / (v1 + v2))
            else:
                t = abs((L - (x1 + x2)) / (v1 + v2))
        print('YES')
        print(t)
        return

    # different dots
    if (x1 + x2) / 2 < L / 2:
        if (v1 + v2) / 2 > 0:
            t1 = abs((L - (x1 + x2))/(v1 + v2))
        else:
            t1 = abs((x1 + x2) / (v1 + v2))
    else:
        if (v1 + v2) / 2 > 0:
            t1 = abs((2 * L - (x1 + x2)) / (v1 + v2))
        else:
            t1 = abs((L - (x1 + x2)) / (v1 + v2))

    # same dot
    if v1 * v2 == 0:
        if x2 > x1 and (v1 > 0 or v2 < 0) or x2 < x1 and (v2 > 0 or v1 < 0):
            t2 = abs((x1 - x2) / (v1 + v2))
        else:
            t2 = abs((L - (min(x1, x2) - max(x1, x2))) / (v1 + v2))
    elif v1 * v2 > 0:
        t2 = abs((x1 - x2) / (v1 - v2))
    else:
        if v1 > 0:
            if x1 < x2:
                t2 = abs((x2 - x1)) / (abs(v1) + abs(v2))
            else:
                t2 = (L - abs((x2 - x1))) / (abs(v1) + abs(v2))
        else:
            if x1 < x2:
                t2 = (L - abs((x2 - x1))) / (abs(v1) + abs(v2))
            else:
                t2 = abs((x2 - x1)) / (abs(v1) + abs(v2))

    t = min(t1, t2)
    print('YES')
    print(t)
    return


# datas = [int(i) for i in input().split()]
# run(*datas)

# run(615_143_346, 79_387_687, -80_123_649, 306_422_480, -80_123_649)
# answer = 2.4075923389

# run(72_036_282, 55_132_452, -373_561_948, 11_464_466, -887_525_183)
# answer = 0.0528091329797

# run(72, 20, -38_121_735, 66, 288_888_467)
# answer = 7.95e-08

# run(10, 7, -3, 1, 4)

# run(55_444_931, 17_419_156, 0, 53_245_822, -398_046_024)
# answer = 0.0382369025

run(1_000_000_000, 10, 1_000_000_000, 11, 0)
# answer = 1e-09

run(5, 0, 0, 1, 2)