"""Task G"""


def cut_up(segments: list[list[int]]) -> int:
    result = []
    for segment in segments:
        lengths = []
        section = []
        sec_min = False
        for n in segment:
            if len(section) == 0:
                section.append(n)
                sec_min = n
                continue
            if n == 1:
                lengths.append(len(section))
                section = [n]
                sec_min = n
            elif n >= len(section) + 1 and sec_min >= len(section) + 1:
                section.append(n)
                if n < sec_min:
                    sec_min = n
            else:
                lengths.append(len(section))
                section = [n]
                sec_min = n
        lengths.append(len(section))
        result.append([len(lengths), lengths])
    return result


def cut_up_input(num=int(input())):
    segments = []
    for i in range(num):
        n = int(input())
        segment = [int(k) for k in input().split()]
        segments.append(segment)

    result = cut_up(segments)
    for segment in result:
        print(segment[0])
        print(' '.join([str(i) for i in segment[1]]))


cut_up_input()

cut_up(segments=[[1, 3, 3, 3, 2], [1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9], [7, 2, 3, 4, 3, 2, 7]])
