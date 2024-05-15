import dataclasses
import pytest

from task_F import change_words


##################
# TEST FOR TASK F
##################


@dataclasses.dataclass
class Case:
    dictionary: set[str]
    words: list[str]
    result: str

    def __str__(self) -> str:
        return f"change_words_{self.dictionary}, {self.words}"


TEST_CASES = [
    Case(dictionary={'a', 'b'}, words=['abdafb', 'basrt', 'casds', 'dsasa', 'a'],
         result='a b casds dsasa a'),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_change_words(t: Case) -> None:
    result = change_words(t.dictionary, t.words)
    assert result == t.result
