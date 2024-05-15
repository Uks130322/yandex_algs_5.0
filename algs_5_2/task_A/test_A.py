import dataclasses
import pytest

from task_A import min_rectangle


##################
# TEST FOR TASK A
##################


@dataclasses.dataclass
class Case:
    coords: list[tuple[int]]
    result: tuple[int]

    def __str__(self) -> str:
        return f"min_rectangle_{self.coords}"


TEST_CASES = [
    Case(coords=[(1, 3), (3, 1), (3, 5), (6, 3)], result=(1, 1, 6, 5))
    ]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_min_rectangle(t: Case) -> None:
    result = min_rectangle(t.coords)
    assert result == t.result
