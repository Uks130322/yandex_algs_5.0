import dataclasses
import pytest

from task_B import sell_fish


##################
# TEST FOR TASK B
##################


@dataclasses.dataclass
class Case:
    n: int
    predict: list[int]
    fresh_days: int
    result: int

    def __str__(self) -> str:
        return f"sell_fish_{self.predict}, {self.fresh_days}"


TEST_CASES = [
    Case(n=5, predict=[1, 2, 3, 4, 5], fresh_days=2, result=2),
    Case(n=5, predict=[5, 4, 3, 2, 1], fresh_days=2, result=0),
    Case(n=8, predict=[1, 2, 3, 4, 5, 3, 2, 1], fresh_days=3, result=3),
    Case(n=3, predict=[1, 3, 4], fresh_days=1, result=2),
]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_sell_fish(t: Case) -> None:
    result = sell_fish(t.n, t.predict, t.fresh_days)
    assert result == t.result
