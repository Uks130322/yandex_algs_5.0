"""Task F"""


def make_odd(n: str, numbers: str) -> str:
    n = int(n)
    numbers = [int(num) for num in numbers.split()]

    remainder = numbers[0] % 2
    result = ''

    for i in range(1, n):
        if numbers[i] % 2:
            if remainder:
                result += 'x'
            else:
                result += '+'
                remainder = 1
        else:
            result += '+'

    return result


print(make_odd(n=input(), numbers=(input())))
