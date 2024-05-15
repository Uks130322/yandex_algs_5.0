import dataclasses
import pytest

from task_B import battleship


##################
# TEST FOR TASK B
##################


@dataclasses.dataclass
class Case:
    field: int
    result: int

    def __str__(self) -> str:
        return f"bin_search_{self.field}"


TEST_CASES = [
    Case(field=7, result=2),
    Case(field=0, result=0),
    Case(field=20, result=3),
    Case(field=50, result=5),
    Case(field=49, result=5),
    Case(field=48, result=4),
    Case(field=1, result=1),
    Case(field=10_000_000_000, result=3912),
    Case(field=117_055_765_888_857_794, result=888887),
    Case(field=100_000_000_000_000_000, result=843430),
    ]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_bin_search(t: Case) -> None:
    result = battleship(t.field)
    assert result == t.result
