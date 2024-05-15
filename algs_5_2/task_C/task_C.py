"""Task C"""


def get_rope(n: int, lengths: list[int]) -> int:
    max_length = max(lengths)
    if max_length * 2 > sum(lengths):
        return max_length * 2 - sum(lengths)
    else:
        return sum(lengths)


def get_rope_input(n=int(input())):
    lengths = [int(i) for i in input().split()]
    print(get_rope(n, lengths))


get_rope_input()
