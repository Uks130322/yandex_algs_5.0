import dataclasses
import pytest

from task_C import add_spaces


##################
# TEST FOR TASK C
##################


@dataclasses.dataclass
class Case:
    n: int
    nums: list[str]
    result: str

    def __str__(self) -> str:
        return f"add_spaces_{self.nums}"


TEST_CASES = [
    Case(n=5, nums=['1', '4', '12', '9', '0'], result='8'),
    Case(n=5, nums=['1', '3', '5', '7', '2'], result='10'),
    Case(n=1, nums=['0'], result='0'),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_add_spaces(t: Case) -> None:
    result = add_spaces(t.n, t.nums)
    assert result == t.result
