"""Task A"""


def min_rectangle(coords: list[tuple[int]]) -> tuple[int]:
    x_min = coords[0][0]
    x_max = coords[0][0]
    y_min = coords[0][1]
    y_max = coords[0][1]
    for x_y in coords:
        if x_y[0] < x_min:
            x_min = x_y[0]
        if x_y[1] > y_max:
            y_max = x_y[1]
        if x_y[0] > x_max:
            x_max = x_y[0]
        if x_y[1] < y_min:
            y_min = x_y[1]

    return x_min, y_min, x_max, y_max


def min_rec_input(n=int(input())):
    coords = []
    for i in range(n):
        x_y = input().split()
        x_y = (int(x_y[0]), int(x_y[1]))
        coords.append(x_y)
    result = [str(i) for i in min_rectangle(coords)]
    result = ' '.join(result)
    print(result)


min_rec_input()
