"""Task G"""


def make_square(coords: list[tuple[int]]) -> tuple:
    coord_set = set(coords)
    if len(coord_set) == 1:
        result = 3
        dots = [(coords[0][0] + 1, coords[0][1]),
                (coords[0][0], coords[0][1] + 1),
                (coords[0][0] + 1, coords[0][1] + 1)]
        return result, dots

    coords = coord_set
    result = 2
    result1 = 2
    dots = []
    dots1 = []

    for (x1, y1) in coords:
        for (x2, y2) in coords:
            if (x1, y1) == (x2, y2):
                continue
            x3 = x2 + (y1 - y2)
            y3 = y2 - (x1 - x2)
            x4 = x1 + (y1 - y2)
            y4 = y1 - (x1 - x2)
            if (x3, y3) in coords:
                if (x4, y4) in coords:
                    result = 0
                    dots = []
                    return result, dots
                else:
                    result1 = 1
                    dots1 = [(x4, y4)]
            elif (x4, y4) in coords:
                result1 = 1
                dots1 = [(x3, y3)]
            else:
                dots = [(x3, y3), (x4, y4)]

    if result1 < result:
        return result1, dots1
    return result, dots


def make_square_input(n=int(input())):
    coords = []
    for i in range(n):
        x, y = input().split()
        coords.append((int(x), int(y)))
    result = make_square(coords)
    dots = [str(x) + ' ' + str(y) for (x, y) in result[1]]
    if dots:
        result = str(result[0]) + '\n' + '\n'.join(dots)
    else:
        result = str(result[0])
    print(result)


make_square_input()
