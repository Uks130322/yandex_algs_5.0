"""Task B"""


def football_comment(first_game: str, second_game: str, first_field: str) -> str:
    first_game = [int(num) for num in first_game.split(':')]
    second_game = [int(num) for num in second_game.split(':')]
    first_field = int(first_field) - 1

    result = first_game[1] + second_game[1] - first_game[0] - second_game[0]

    if first_field:
        additive = int(first_game[0] - second_game[1] <= 0)
    else:
        additive = int(second_game[0] - first_game[1] + result <= 0)

    if result < 0:
        return '0'
    elif result == 0:
        return str(additive)
    else:
        return str(result + additive)


print(football_comment(first_game=input(), second_game=input(), first_field=input()))
