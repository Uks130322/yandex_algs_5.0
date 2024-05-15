import dataclasses
import pytest

from task_I import move_the_ships


##################
# TEST FOR TASK I
##################


@dataclasses.dataclass
class Case:
    size: int
    ships: list[list[int]]
    result: int

    def __str__(self) -> str:
        return f"move_the_ships_{self.ships}"


TEST_CASES = [
    Case(size=3, ships=[[1, 2], [3, 3], [1, 1]], result=3),
    Case(size=10, ships=[[4, 4], [10, 2], [5, 5], [5, 1], [1, 8], [9, 3], [9, 6], [8, 5], [1, 9], [4, 5]], result=23),

]


@pytest.mark.parametrize("t", TEST_CASES, ids=str)
def test_move_the_ships(t: Case) -> None:
    result = move_the_ships(t.size, t.ships)
    assert result == t.result
