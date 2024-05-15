import dataclasses
import pytest

from task_D import get_perimeter


##################
# TEST FOR TASK D
##################


@dataclasses.dataclass
class Case:
    n: int
    coords: list[tuple[int]]
    result: int

    def __str__(self) -> str:
        return f"get_perimeter_{self.coords}"


TEST_CASES = [
    Case(n=3, coords=[(1, 1), (1, 2), (2, 1)], result=8),
    Case(n=1, coords=[(8, 8)], result=4),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_get_perimeter(t: Case) -> None:
    result = get_perimeter(t.n, t.coords)
    assert result == t.result
