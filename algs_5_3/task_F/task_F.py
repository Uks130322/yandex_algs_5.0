"""Task F"""


def change_words(dictionary: set[str], words: list[str]) -> str:
    result = ''
    for word in words:
        for i in range(len(word)):
            if word[:i] in dictionary:
                result += word[:i] + " "
                break
        else:
            result += word + " "
    return result[:-1]


def change_words_input():
    dictionary = set(input().split())
    words = list(input().split())
    result = change_words(dictionary, words)
    print(result)


change_words_input()
