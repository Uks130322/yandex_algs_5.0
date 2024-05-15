import dataclasses
import pytest

from task_D import find_repeat


##################
# TEST FOR TASK D
##################


@dataclasses.dataclass
class Case:
    k: int
    nums: list[int]
    result: int

    def __str__(self) -> str:
        return f"find_repeat_{self.k}, {self.nums}"


TEST_CASES = [
    Case(k=2, nums=[1, 2, 3, 1], result="NO"),
    Case(k=1, nums=[1, 0, 1, 1], result="YES"),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_find_repeat(t: Case) -> None:
    result = find_repeat(t.k, t.nums)
    assert result == t.result
