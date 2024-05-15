"""Task E"""


def raise_the_snail(n: int, berries: list[list[int]]) -> int:
    berries = [[i + 1] + item for i, item in enumerate(berries)]
    good_berries = []
    bad_berries = []
    for berry in berries:
        if berry[1] - berry[2] > 0:
            good_berries.append(berry)
        else:
            bad_berries.append(berry)
    good_berries = sorted(good_berries, key=lambda item: item[2])
    bad_berries = sorted(bad_berries, key=lambda item: item[1], reverse=True)
    max_height = 0
    height = 0
    for (i, up, down) in good_berries + bad_berries:
        height += up
        if height > max_height:
            max_height = height
        height -= down
    return max_height, [berry[0] for berry in good_berries + bad_berries]


def raise_the_snail_input(n=int(input())):
    berries = list()
    for i in range(n):
        x_y = input().split()
        x_y = [int(x_y[0]), int(x_y[1])]
        berries.append(x_y)

    result = raise_the_snail(n, berries)
    print(result[0])
    print(' '.join(str(i) for i in result[1]))


raise_the_snail_input()

# print(raise_the_snail(4, [[8, 2], [3, 2], [2, 1], [5, 3]]))
