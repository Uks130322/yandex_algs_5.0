import dataclasses
import pytest

from task_E import raise_the_snail


##################
# TEST FOR TASK E
##################


@dataclasses.dataclass
class Case:
    n: int
    berries: list[list[int]]
    result: (int, list[int])

    def __str__(self) -> str:
        return f"get_perimeter_{self.berries}"


TEST_CASES = [
    Case(n=3, berries=[[1, 5], [8, 2], [4, 4]], result=(10, [2, 3, 1])),
    Case(n=1, berries=[[7, 6]], result=(7, [1])),
    Case(n=4, berries=[[8, 2], [3, 2], [2, 1], [5, 3]], result=(13, [3, 1, 2, 4])),
    Case(n=2, berries=[[7, 6], [7, 4]], result=(10, [2, 1])),
    Case(n=7, berries=[[160714711, 449656269], [822889311, 446755913], [135599877, 389312924],
                       [480845266, 448565595], [561330066, 605997004], [61020590, 573085537],
                       [715477619, 181424399]], result=(1503796355, [2, 4, 7, 5, 1, 3, 6])),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_raise_the_snail(t: Case) -> None:
    result = raise_the_snail(t.n, t.berries)
    assert result == t.result
