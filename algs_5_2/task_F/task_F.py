"""Task F"""


def spin_to_win(sectors: int, sector_list: list[int], min_v: int, max_v: int, slow_down: int) -> int:
    max_win = 0
    min_spin = min_v // slow_down - int(not bool(min_v % slow_down))
    max_spin = max_v // slow_down
    if min_spin == max_spin:
        result_1 = sector_list[min_spin % sectors]
        if result_1 > max_win:
            max_win = result_1
        result_2 = sector_list[-(min_spin % sectors)]
        if result_2 > max_win:
            max_win = result_2
        return max_win

    if (max_v - min_v) / slow_down > sectors:
        return max(sector_list)

    for num in range(min_spin, max_spin + int(bool(max_v % slow_down))):
        result_1 = sector_list[num % sectors]
        if result_1 > max_win:
            max_win = result_1
        result_2 = sector_list[-(num % sectors)]
        if result_2 > max_win:
            max_win = result_2

    return max_win


def spin_for_win_input(sectors=int(input())):
    sector_list = [int(i) for i in input().split()]
    min_v, max_v, slow_down = (int(i) for i in input().split())

    result = spin_to_win(sectors, sector_list, min_v, max_v, slow_down)
    print(result)


spin_for_win_input()

print(spin_to_win(sectors=4, sector_list=[744, 43, 468, 382], min_v=20, max_v=48, slow_down=12))

# print("first", num, result_1)
# print("second", num, result_2)
