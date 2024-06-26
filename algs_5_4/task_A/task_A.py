"""Task A"""


def bin_bin_search(N: int, lst: list[int], num: tuple[int]):
    left1 = 0
    right1, right2 = N - 1, N - 1
    n1, n2 = num[0], num[1]

    while left1 < right1:
        print(left1, right1)
        middle = (left1 + right1) // 2
        if lst[left1] >= n1:
            right1 = left1
        elif right1 - left1 == 1:
            left1 = right1
        elif lst[middle] < n1:
            left1 = middle
        else:
            right1 = middle

    left2 = right1

    while left2 < right2:
        print('two', left2, right2)
        middle = (left2 + right2) // 2
        if lst[right2] <= n2:
            left2 = right2
        elif right2 - left2 == 1:
            right2 = left2
        elif lst[middle] <= n2:
            left2 = middle
        else:
            right2 = middle
    if right2 == left1 and not (n1 <= lst[right2] <= n2):
        return 0
    return right2 - left1 + 1


# def search_in_list_input(n=int(input())):
#     lst = sorted([int(i) for i in input().split()])
#     k = int(input())
#     result = []
#     for i in range(k):
#         num = tuple(int(i) for i in input().split())
#         result.append(str(bin_bin_search(n, lst, num)))
#     print(' '.join(result))
#
#
# search_in_list_input()


# print(bin_bin_search(3, lst=[-100, 0, 100], num=(1, 99)))
# print(bin_bin_search(100, [-10, -10, -10, -10, -10, -9, -9, -8, -8, -8,
#                            -8, -7, -7, -7, -7, -6, -6, -6, -5, -5,
#                            -5, -4, -4, -4, -3, -2, -2, -2, -2, -2,
#                            -2, -2, -1, -1, -1, -1, 0, 0, 0, 0,
#                            1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
#                            2, 2, 2, 2, 3, 3, 3, 3, 3, 4,
#                            4, 4, 4, 4, 4, 5, 5, 5, 5, 6,
#                            6, 6, 6, 6, 6, 6, 7, 7, 7, 7,
#                            8, 8, 8, 8, 8, 9, 9, 9, 9, 9,
#                            9, 9, 9, 9, 9, 10, 10, 10, 10, 10],
#                      num=(-8, 5))
#       )
big_list = [-994336796, -954074896, -951250662, -913951858, -911943482, -879588578, -830035090, -825009360,
            -802712434, -757673692, -730626988, -683211300, -639954654, -635747004, -622165778, -601807632,
            -576446286, -553984774, -545913794, -539185372, -519967062, -514488566, -500021710, -483406258,
            -469396156, -457079332, -397474768, -382889098, -339497926, -267026586, -263351768, -230300990,
            -215080950, -211151198, -177966474, -169155846, -154753312, -124816466, -106990434, -100208468,
            -98993800, -89156334, -47739222, -38748050, -23148936, -12506528, -7678370, 1010116, 26241386,
            35465760, 58058066, 108154874, 126255048, 139055284, 182078872, 213000560, 220436502, 244154006,
            250479818, 258730634, 272439736, 306959942, 311595998, 311873826, 336527960, 342368462, 368407986,
            376025256, 376363446, 385685840, 420292782, 470334958, 482001042, 488819408, 489069462, 507454908,
            510320588, 567805062, 571196544, 592827252, 594766870, 661544136, 712292236, 721216724, 735149712,
            784588618, 792130688, 836975304, 840569556, 862514348, 873550146, 877507706, 880187206, 880535016,
            943465840, 948745422, 968183320, 969899438, 981979332, 997919610]

nums_list = [(-995518640, -296147906)]

for num in nums_list:
    print(bin_bin_search(100, big_list, num))
