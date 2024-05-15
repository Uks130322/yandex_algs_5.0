import dataclasses
import pytest

from task_C import delete_nums


##################
# TEST FOR TASK C
##################


@dataclasses.dataclass
class Case:
    nums: list[int]
    result: int

    def __str__(self) -> str:
        return f"delete_nums_{self.nums}"


TEST_CASES = [
    Case(nums=[1, 2, 3, 4, 5], result=3),
    Case(nums=[1, 1, 2, 3, 5, 5, 2, 2, 1, 5], result=4),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_delete_nums(t: Case) -> None:
    result = delete_nums(t.nums)
    assert result == t.result
