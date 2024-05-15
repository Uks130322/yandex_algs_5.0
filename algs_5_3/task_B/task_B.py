"""Task B"""


def anagram(word1: str, word2: str) -> str:
    dict1 = dict()
    for char in word1:
        dict1[char] = dict1.get(char, 0) + 1
    dict2 = dict()
    for char in word2:
        dict2[char] = dict2.get(char, 0) + 1
    if dict1 == dict2:
        return "YES"
    else:
        return "NO"


def anagram_input():
    word1 = input()
    word2 = input()
    result = anagram(word1, word2)
    print(result)


anagram_input()
