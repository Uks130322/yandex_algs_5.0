"""Task B"""


def battleship(field: int) -> int:
    if field <= 1:
        return field
    min_k = 0
    max_k = round(field ** 0.5) + 1
    while min_k < max_k:
        if max_k - min_k == 1:
            return min_k
        middle = (min_k + max_k) // 2
        len_middle = get_length(middle)
        if len_middle == field:
            return middle
        elif len_middle > field:
            max_k = middle
        else:
            min_k = middle

    return max_k


def get_length(k):
    if k == 1:
        length = 1
    elif k == 2:
        length = 6
    else:
        length = (k + 2) * (k ** 2 + k * 4 - 3)//6
    return length



print(battleship(int(input())))

# print(get_length(0))
print(get_length(1))
print(get_length(2))
print(get_length(k=3))
print(get_length(4))
print(get_length(5))
print(get_length(6))
# print(get_length(7))
# print(get_length(8))
# print(get_length(9))
print(get_length(888888))


# def get_length(k):
"""it's working too, but slower"""
# sum_length = 0
# for i in range(1, k + 1):
#     length = (i + 1) * i // 2 + i
#     sum_length += length
# return max(sum_length - 1, 0)
