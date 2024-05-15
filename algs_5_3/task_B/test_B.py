import dataclasses
import pytest

from task_B import anagram


##################
# TEST FOR TASK B
##################


@dataclasses.dataclass
class Case:
    word1: str
    word2: str
    result: str

    def __str__(self) -> str:
        return f"playlists_{self.word1}, {self.word2}"


TEST_CASES = [
    Case(word1='dusty', word2='study', result="YES"),
    Case(word1='rat', word2='bat', result="NO"),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_playlists(t: Case) -> None:
    result = anagram(t.word1, t.word2)
    assert result == t.result
