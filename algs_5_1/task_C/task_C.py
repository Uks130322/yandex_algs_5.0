"""Task C"""


def add_spaces(n: int, nums: list[str]) -> str:
    result = 0
    for i in range(n):
        num = int(nums[i])
        result += num // 4 + num % 4 // 3 * 2 + num % 4 % 3
    return str(result)


def add_spaces_with_input():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    print(add_spaces(n, nums))


add_spaces_with_input()
