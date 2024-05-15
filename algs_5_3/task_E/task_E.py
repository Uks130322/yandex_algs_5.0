def find_repeat(nums: list[set[int]]) -> int:
    result = (nums[0] & nums[1]) | (nums[0] & nums[2]) | (nums[1] & nums[2])
    return sorted(list(result))


def find_repeat_input():
    n = input()
    nums = [set(int(i) for i in input().split())]
    n = input()
    nums.append(set(int(i) for i in input().split()))
    n = input()
    nums.append(set(int(i) for i in input().split()))
    result = find_repeat(nums)
    print(' '.join(str(i) for i in result))


find_repeat_input()