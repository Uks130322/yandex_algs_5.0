"""Task D"""


def find_repeat(k: int, nums: list[int]) -> str:
    nums_dict = dict()
    count = 0
    for num in nums:
        if num in nums_dict.keys():
            if count - nums_dict[num] <= k:
                return "YES"
        nums_dict[num] = count
        count += 1
    return "NO"


def find_repeat_input():
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    result = find_repeat(k, nums)
    print(result)


find_repeat_input()
