import dataclasses
import pytest

from task_A import bin_bin_search


##################
# TEST FOR TASK A
##################


@dataclasses.dataclass
class Case:
    N: int
    lst: list[int]
    num: tuple[int]
    result: int

    def __str__(self) -> str:
        return f"bin_search_{self.lst}, {self.num}"


TEST_CASES = [
    Case(N=5, lst=[1, 3, 4, 10, 10], num=(1, 10), result=5),
    Case(N=5, lst=[1, 3, 4, 10, 10], num=(2, 9), result=2),
    Case(N=5, lst=[1, 3, 4, 10, 10], num=(3, 4), result=2),
    Case(N=5, lst=[1, 3, 4, 10, 10], num=(2, 2), result=0),
    ]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_bin_search(t: Case) -> None:
    result = bin_bin_search(t.N, t.lst, t.num)
    assert result == t.result
