"""Task I"""


def move_the_ships(size: int, ships: list[list[int]]) -> int:
    middle = sum([j for [i, j] in ships]) // size
    i_list = [i for [i, j] in ships]
    i_list = sorted(i_list)
    vert_move = 0
    for n in range(1, size + 1):
        vert_move += abs(n - i_list[n - 1])
    hor_list = []
    for n in range(1, size + 1):
        hor_move = 0
        for ship in ships:
            hor_move += abs(ship[1] - n)
        hor_list.append(hor_move)
    return vert_move + min(hor_list)


def move_the_ships_input(size=int(input())):
    ships = []
    for i in range(size):
        ship = [int(i) for i in input().split()]
        ships.append(ship)

    result = move_the_ships(size, ships)
    print(result)


move_the_ships_input()


# print(move_the_ships(size=3, ships=[[1, 2], [3, 3], [1, 1]]))
