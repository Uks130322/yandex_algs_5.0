"""Task H"""


def fury_of_the_elves(race: int, classes: int, race_class: list[list[int]]) -> tuple[int]:
    max1 = 0
    max2 = 0
    i1, i2, j1, j2 = 0, 0, 0, 0
    for i in range(race):
        for j in range(classes):
            if race_class[i][j] > max1:
                max2 = max1
                i2 = i1
                j2 = j1
                max1 = race_class[i][j]
                i1 = i
                j1 = j
            elif race_class[i][j] > max2:
                max2 = race_class[i][j]
                i2 = i
                j2 = j
    if i1 == i2:
        result = []
        for j1 in range(classes):
            string3 = [race_class[i][j1] for i in range(race) if i != i1]
            max3 = max(string3)
            max3_num = string3.count(max3)
            result.append([j1, max3, max3_num])
        max3 = max([i[1] for i in result])
        result = [i for i in result if i[1] == max3]
        result = sorted(result, key=lambda item: item[2])[0]
        return i1 + 1, result[0] + 1
    if j1 == j2:
        result = []
        for i1 in range(race):
            string3 = [race_class[i1][j] for j in range(classes) if j != j1]
            max3 = max(string3)
            max3_num = string3.count(max3)
            result.append([i1, max3, max3_num])
        max3 = max([i[1] for i in result])
        result = [i for i in result if i[1] == max3]
        result = sorted(result, key=lambda item: item[2])[0]
        return result[0] + 1, j1 + 1

    string3 = ([race_class[i1][j] for j in range(classes) if j != j1] +
               [race_class[i][j2] for i in range(race) if i != i2])
    max3 = max(string3)
    string4 = ([race_class[i2][j] for j in range(classes) if j != j2] +
               [race_class[i][j1] for i in range(race) if i != i1])
    max4 = max(string4)
    if max3 == max4:
        max3_num = string3.count(max3)
        max4_num = string3.count(max4)
        if max3_num > max4_num:
            return i1 + 1, j2 + 1
        else:
            return i2 + 1, j1 + 1
    if max3 > max4:
        return i1 + 1, j2 + 1
    else:
        return i2 + 1, j1 + 1


def fury_of_the_elves_input():
    race, classes = [int(i) for i in input().split()]
    race_class = []
    for i in range(race):
        class_string = [int(i) for i in input().split()]
        race_class.append(class_string)

    result = fury_of_the_elves(race, classes, race_class)
    print(str(result[0]), str(result[1]))


fury_of_the_elves_input()


# print(fury_of_the_elves(race=2, classes=2, race_class=[[1, 2], [3, 4]]))
