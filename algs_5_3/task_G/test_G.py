import dataclasses
import pytest

from task_G import make_square


##################
# TEST FOR TASK G
##################


@dataclasses.dataclass
class Case:
    coords: list[tuple[int]]
    result: tuple[int, list[tuple[int]]]

    def __str__(self) -> str:
        return f"make_square_{self.coords}"


TEST_CASES = [
    Case(coords=[(0, 1), (1, 0)], result=(2, [(0, 0), (1, 1)])),
    Case(coords=[(0, 2), (2, 0), (2, 2)], result=(1, [(0, 0)])),
    Case(coords=[(-1, 1), (1, 1), (-1, -1), (1, -1)], result=(0, [])),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_make_square(t: Case) -> None:
    result = make_square(t.coords)
    assert result == t.result
