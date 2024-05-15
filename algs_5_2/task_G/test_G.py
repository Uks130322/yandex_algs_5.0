import dataclasses
import pytest

from task_G import cut_up


##################
# TEST FOR TASK G
##################


@dataclasses.dataclass
class Case:
    segments: list[list[int]]
    result: list[list[int, list[int]]]

    def __str__(self) -> str:
        return f"cut_up_{self.segments}"


TEST_CASES = [
    Case(segments=[[1, 3, 3, 3, 2], [1, 9, 8, 7, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9], [7, 2, 3, 4, 3, 2, 7]],
         result=[[3, [1, 3, 1]], [3, [1, 6, 9]], [3, [2, 3, 2]]]),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_cut_up(t: Case) -> None:
    result = cut_up(t.segments)
    assert result == t.result
