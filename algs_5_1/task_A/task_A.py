"""Task A"""


def tree_painter(vasya, masha):
    vasya = [int(num) for num in vasya.split(' ')]  # begin and end of vasya's interval
    masha = [int(num) for num in masha.split(' ')]  # begin and end of masha's interval
    v = [vasya[0] - vasya[1], vasya[0] + vasya[1]]
    m = [masha[0] - masha[1], masha[0] + masha[1]]

    if v[1] < m[0] or v[0] > m[1]:  # intervals do not intersect
        result = abs(v[1] - v[0]) + abs(m[1] - m[0]) + 2

    else:
        datas = v + m
        result = abs(max(datas) - min(datas)) + 1

    return str(result)


print(tree_painter(vasya=input(), masha=input()))
