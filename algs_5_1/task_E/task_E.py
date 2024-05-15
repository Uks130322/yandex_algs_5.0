"""Task E"""


def startup(profit: str, founders: str, days: str) -> str:
    if len(founders) - len(profit) > 1 or int(days) < 1:
        return '-1'

    for i in range(10):
        if int(profit + str(i)) % int(founders) == 0:
            return str(int(profit + str(i))) + '0' * (int(days) - 1)

    return '-1'


profit, founders, days = input().split()
print(startup(profit, founders, days))
