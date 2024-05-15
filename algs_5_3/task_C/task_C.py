"""Task C"""


def delete_nums(nums: list[int]) -> int:
    nums_dict = dict()
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    result_dict = dict()
    for key in nums_dict.keys():
        if key + 1 in nums_dict.keys():
            result_dict[key] = nums_dict[key] + nums_dict[key + 1]
        elif key not in result_dict.keys():
            result_dict[key] = nums_dict[key]
    return len(nums) - max(result_dict.values())


def delete_nums_input(n=int(input())):
    nums = [int(i) for i in input().split()]
    result = delete_nums(nums)
    print(result)


delete_nums_input()
