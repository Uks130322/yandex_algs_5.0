"""Task J"""


def recolor(field: list[list[str]], i1: int, j1: int, i2: int, j2: int, color: str, start_color="#"):
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if field[i][j] == start_color:
                field[i][j] = color
            else:
                return False
    return field


def find_coords(field: list[list[str]], i_max: int, j_max: int, i1: int, j1: int):
    i2, j2 = i1, j1
    while True:
        if i2 + 1 < i_max and field[i2 + 1][j1] == '#':
            i2 += 1
            continue
        else:
            if j2 + 1 < j_max and field[i2][j2 + 1] == '#':
                j2 += 1
                continue
            else:
                return i2, j2


def is_lattice(field: list[list[str]]):
    for sting in field:
        if "#" in sting:
            return True
    return False


def two_rectangles(i_max, j_max, field: list[list[str]], is_rotated=False, is_mirrored=False) -> str:
    if not is_lattice(field):
        return "NO"
    else:
        first_rec = []
        for i in range(i_max):
            for j in range(j_max):
                if field[i][j] != "#":
                    continue
                elif field[i][j] == "#":
                    i1, j1 = i, j
                    i2, j2 = find_coords(field, i_max, j_max, i1, j1)
                    new_field = recolor(field, i1, j1, i2, j2, "a")
                    if not new_field:
                        return "NO"
                    else:
                        field = new_field
                        first_rec = [i1, j1, i2, j2]
                        break
            if first_rec:
                break

        if is_lattice(field):
            second_rec = []
            for i in range(i_max):
                for j in range(j_max):
                    if field[i][j] == "#":
                        i1, j1 = i, j
                        i2, j2 = find_coords(field, i_max, j_max, i1, j1)
                        new_field = recolor(field, i1, j1, i2, j2, "b")
                        if not new_field:
                            return "NO"
                        else:
                            field = new_field
                            second_rec = True
                            break
                if second_rec:
                    break

            if is_lattice(field):
                return "NO"
            else:
                if is_rotated:
                    field = list(map(list, reversed(list(zip(*field)))))
                if is_mirrored:
                    field = [item[::-1] for item in field]
                result = "\n".join([''.join(string) for string in field])
                return "YES\n" + result
        else:
            if first_rec[:2] == first_rec[2:]:
                return "NO"
            else:
                if first_rec[1] == first_rec[3]:
                    field = recolor(field, first_rec[0] + 1, first_rec[1],
                                    first_rec[2], first_rec[3], "b", start_color="a")
                    if is_rotated:
                        field = list(map(list, reversed(list(zip(*field)))))
                    if is_mirrored:
                        field = [item[::-1] for item in field]
                    result = "\n".join([''.join(string) for string in field])
                    return "YES\n" + result
                else:
                    field = recolor(field, first_rec[0], first_rec[1] + 1,
                                    first_rec[2], first_rec[3], "b", start_color="a")
                    if is_rotated:
                        field = list(map(list, reversed(list(zip(*field)))))
                    if is_mirrored:
                        field = [item[::-1] for item in field]
                    result = "\n".join([''.join(string) for string in field])
                    return "YES\n" + result


def two_rectangles_input():
    i_max, j_max = [int(i) for i in input().split()]
    field = []
    for i in range(i_max):
        lst = list(input())
        field.append(lst)
    i2_max, j2_max = j_max, i_max
    field2 = list(map(list, zip(*field[::-1])))
    field3 = [item[::-1] for item in field]
    result1 = two_rectangles(i_max, j_max, field)
    result2 = two_rectangles(i2_max, j2_max, field2, is_rotated=True)
    result3 = two_rectangles(i_max, j_max, field3, is_mirrored=True)
    if result1 == "NO":
        if result2 == "NO":
            print(result3)
        else:
            print(result2)
    else:
        print(result1)


two_rectangles_input()


# print(two_rectangles(2, 1, [["#"], ["."]]))
