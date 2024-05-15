"""Task G
Need to refactor but do work"""

# print(my_solders, casern, enemies)


def destroy_with_pass(my_solders: int, casern: int, enemies: int, num: int) -> int:
    result = 1
    casern -= my_solders

    if casern <= 0:
        return result

    while casern > 0 or enemies > 0:
        if my_solders * 2 < enemies:

            result = -1
            break
        if my_solders >= casern + enemies:
            result += 1
            break
        if casern > 0:
            if my_solders == enemies:

                if my_solders < enemies - casern:
                    result = -1
                    break
                else:
                    enemies -= my_solders - casern
                    casern = 0
                    my_solders -= enemies
                    result += 1
                    continue
            if (my_solders - (enemies - (my_solders - casern)) - 1) * 3 >= enemies - (my_solders - casern):
                if (num > 0 and (result > 1 or result == 1 and
                                 (my_solders - (enemies - (my_solders - casern))) /
                                 (enemies - (my_solders - casern)) < 2)):
                    print('im here')
                    casern -= my_solders - enemies
                    result += 1
                    num -= 1
                    continue
                enemies -= my_solders - casern
                casern = 0
                my_solders -= enemies
                result += 1
            else:
                if my_solders <= enemies:
                    result = -1
                    break
                casern -= my_solders - enemies
                result += 1
        else:
            enemies -= my_solders
            my_solders -= enemies
            result += 1

    return result


def destroy(my_solders: int, casern: int, enemies: int) -> int:
    if my_solders - enemies <= 0:
        limit = 2
    else:
        limit = casern // (my_solders - enemies) // 2 + 1
    results = [destroy_with_pass(my_solders, casern, enemies, num) for num in range(limit)]
    if max(results) == -1:
        return -1
    else:
        results = [i for i in results if i != -1]
    return min(results)


# print(destroy(int(input()), int(input()), int(input())))
# print(destroy_with_pass(250, 500, 234))
# print(destroy(250, 500, 187))
# print(destroy(250, 500, 240))
# print(destroy(499, 500, 499))
print(destroy(10, 11, 15))
# print(destroy(3000, 5000, 2998))


# print(destroy(5, 7, 10))
