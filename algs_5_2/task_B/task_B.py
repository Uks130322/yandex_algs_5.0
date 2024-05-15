"""Task A"""


def sell_fish(n: int, predict: list[int], fresh_days: int) -> int:
    result = 0
    for day, price in enumerate(predict):
        for i in range(day, min((day + fresh_days + 1), n)):
            if predict[i] - price > result:
                result = predict[i] - price
    return result


def sell_fish_input():
    predict_days, fresh_days = [int(i) for i in input().split()]
    predict = [int(i) for i in input().split()]
    print(sell_fish(predict_days, predict, fresh_days))


sell_fish_input()

print(sell_fish(n=5, predict=[5, 4, 3, 2, 1], fresh_days=2))
