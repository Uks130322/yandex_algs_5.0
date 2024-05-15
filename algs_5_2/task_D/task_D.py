"""Task D"""


def get_neighbors(x, y):
    return (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)


def get_perimeter(n: int, coords: set[tuple[int]]) -> int:
    perimeter = n * 4
    counted_dots = set()
    for (x, y) in coords:
        for (x1, y1) in get_neighbors(x, y):
            if (x1, y1) in counted_dots:
                perimeter -= 2
            else:
                counted_dots.add((x, y))
    return perimeter


def get_perimeter_input(n=int(input())):
    coords = set()
    for i in range(n):
        x_y = input().split()
        x_y = (int(x_y[0]), int(x_y[1]))
        coords.add(x_y)
    print(get_perimeter(n, coords))


get_perimeter_input()
